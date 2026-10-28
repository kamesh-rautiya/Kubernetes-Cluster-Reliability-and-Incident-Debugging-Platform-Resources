#!/usr/bin/env python3
"""
KubeRescue Safety Guards
Prevents destructive commands and enforces namespace restrictions
"""

import re
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm

console = Console()

# Dangerous patterns that should be blocked
DANGEROUS_PATTERNS = [
    # Deleting critical namespaces
    {
        "pattern": r"kubectl\s+delete\s+namespace\s+(kube-system|kube-public|kube-node-lease|default)",
        "message": "🚨 BLOCKED: Cannot delete critical system namespaces!",
        "severity": "critical"
    },
    # Deleting kuberescue namespace (warn)
    {
        "pattern": r"kubectl\s+delete\s+namespace\s+kuberescue",
        "message": "⚠️  WARNING: This will delete the entire kuberescue namespace and all your work!",
        "severity": "warning"
    },
    # Deleting nodes
    {
        "pattern": r"kubectl\s+delete\s+node",
        "message": "🚨 BLOCKED: Cannot delete cluster nodes!",
        "severity": "critical"
    },
    # Deleting all resources in namespace
    {
        "pattern": r"kubectl\s+delete\s+\w+\s+--all",
        "message": "⚠️  WARNING: This will delete ALL resources of this type in the namespace!",
        "severity": "warning"
    },
    # Cluster-wide deletions
    {
        "pattern": r"kubectl\s+delete\s+.*\s+--all-namespaces",
        "message": "🚨 BLOCKED: Cannot delete resources across all namespaces!",
        "severity": "critical"
    },
    # CRDs
    {
        "pattern": r"kubectl\s+delete\s+crd",
        "message": "🚨 BLOCKED: Cannot delete CustomResourceDefinitions!",
        "severity": "critical"
    },
    # ClusterRoles and ClusterRoleBindings
    {
        "pattern": r"kubectl\s+delete\s+(clusterrole|clusterrolebinding)",
        "message": "🚨 BLOCKED: Cannot delete cluster-level RBAC resources!",
        "severity": "critical"
    },
    # PersistentVolumes (not PVCs)
    {
        "pattern": r"kubectl\s+delete\s+pv\s+",
        "message": "⚠️  WARNING: Deleting PersistentVolumes can cause data loss!",
        "severity": "warning"
    },
]

# Namespaces that should be used in KubeRescue
ALLOWED_NAMESPACES = ["kuberescue", "default"]

# Commands that require confirmation
RISKY_COMMANDS = [
    r"kubectl\s+delete\s+namespace",
    r"kubectl\s+drain\s+node",
    r"kubectl\s+cordon\s+node",
]


def check_command_safety(command: str) -> tuple[bool, str, str]:
    """
    Check if a command is safe to run
    
    Returns:
        (is_safe, message, severity)
    """
    command_lower = command.lower().strip()
    
    # Check dangerous patterns
    for pattern_def in DANGEROUS_PATTERNS:
        if re.search(pattern_def["pattern"], command_lower, re.IGNORECASE):
            return False, pattern_def["message"], pattern_def["severity"]
    
    # Check if command targets the wrong namespace
    if "kubectl" in command_lower:
        # Extract namespace from -n or --namespace flag
        namespace_match = re.search(r"(-n|--namespace)\s+(\S+)", command_lower)
        
        # If namespace is specified, check if it's allowed
        if namespace_match:
            namespace = namespace_match.group(2)
            if namespace not in ALLOWED_NAMESPACES:
                return (
                    False,
                    f"⚠️  WARNING: KubeRescue should use namespace 'kuberescue', not '{namespace}'",
                    "warning"
                )
    
    return True, "", "safe"


def is_command_risky(command: str) -> bool:
    """Check if command requires user confirmation"""
    command_lower = command.lower().strip()
    
    for pattern in RISKY_COMMANDS:
        if re.search(pattern, command_lower, re.IGNORECASE):
            return True
    
    return False


def validate_kubectl_command(command: str, interactive: bool = True) -> bool:
    """
    Validate a kubectl command before execution
    
    Args:
        command: The command to validate
        interactive: If True, ask for confirmation on risky commands
    
    Returns:
        True if command should be executed, False if blocked
    """
    is_safe, message, severity = check_command_safety(command)
    
    if not is_safe:
        if severity == "critical":
            # Block completely
            console.print(Panel(
                f"[bold red]{message}[/bold red]\n\n"
                "[yellow]This command is blocked for your safety.[/yellow]\n"
                "[dim]KubeRescue limits operations to the 'kuberescue' namespace.[/dim]",
                title="[bold red]⛔ Safety Guard Activated[/bold red]",
                border_style="red"
            ))
            return False
        
        elif severity == "warning" and interactive:
            # Ask for confirmation
            console.print(Panel(
                f"[bold yellow]{message}[/bold yellow]\n\n"
                "[dim]This operation may have unintended consequences.[/dim]",
                title="[bold yellow]⚠️  Caution Required[/bold yellow]",
                border_style="yellow"
            ))
            
            if not Confirm.ask("Are you sure you want to proceed?", default=False):
                console.print("[dim]Command cancelled.[/dim]")
                return False
    
    # Check if risky (but not blocked)
    if interactive and is_command_risky(command):
        console.print(Panel(
            f"[yellow]This is a risky operation:[/yellow]\n"
            f"[cyan]{command}[/cyan]\n\n"
            "[dim]Please confirm you want to proceed.[/dim]",
            title="[bold yellow]⚠️  Confirmation Required[/bold yellow]",
            border_style="yellow"
        ))
        
        if not Confirm.ask("Execute this command?", default=False):
            console.print("[dim]Command cancelled.[/dim]")
            return False
    
    return True


def print_safety_info():
    """Print information about safety guards"""
    info = """
# 🛡️  KubeRescue Safety Guards

KubeRescue protects you from dangerous operations:

## 🚫 Blocked Commands:
- Deleting critical namespaces (kube-system, default, etc.)
- Deleting cluster nodes
- Deleting CustomResourceDefinitions
- Cluster-wide deletions (--all-namespaces)
- Deleting ClusterRoles/ClusterRoleBindings

## ⚠️  Commands Requiring Confirmation:
- Deleting namespaces
- Draining nodes
- Deleting all resources (--all)
- PersistentVolume operations

## ✅ Best Practices:
- Always use `-n kuberescue` namespace flag
- Avoid cluster-wide operations
- Test changes before applying
- Use `kubectl apply` instead of `kubectl create`

## 🔓 Disabling Safety Guards:
Safety guards can be bypassed with:
    export KUBERESCUE_SAFETY=off

But we **strongly recommend** keeping them enabled!
    """
    
    from rich.markdown import Markdown
    console.print(Panel(
        Markdown(info),
        title="[bold green]Safety Information[/bold green]",
        border_style="green"
    ))


def main():
    """CLI tool for testing safety checks"""
    if len(sys.argv) < 2:
        print_safety_info()
        return
    
    if sys.argv[1] == "info":
        print_safety_info()
        return
    
    # Test a command
    command = " ".join(sys.argv[1:])
    console.print(f"\n[cyan]Testing command:[/cyan] {command}\n")
    
    if validate_kubectl_command(command, interactive=True):
        console.print("[green]✅ Command passed safety checks[/green]\n")
    else:
        console.print("[red]❌ Command blocked by safety guards[/red]\n")


if __name__ == "__main__":
    main()

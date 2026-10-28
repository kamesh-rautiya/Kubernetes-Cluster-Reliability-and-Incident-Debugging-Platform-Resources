# KubeRescue 🕹️⚙️ — Kubernetes Cluster Reliability & Incident Debugging Platform

[![Platform Support](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-blue)]()
[![Shell](https://img.shields.io/badge/shell-bash-green)]()
[![Kubernetes](https://img.shields.io/badge/kubernetes-learning-326CE5)]()
[![Docker](https://img.shields.io/badge/docker-enabled-2496ED)]()
[![kubectl](https://img.shields.io/badge/kubectl-CLI-326CE5)]()
[![Kind](https://img.shields.io/badge/kind-multi--node-orange)]()

**Designed and resolved 50+ simulated cluster outages** across Kind and multi-node setups, systematically troubleshooting Pod lifecycles, DNS resolution, and CNI/storage failures.

KubeRescue is an **interactive Kubernetes incident debugging platform** built with a retro arcade-style terminal UI. Each mission simulates a real-world cluster outage — you diagnose the root cause and apply the fix using `kubectl`, declarative manifests, and Linux system internals.

**50 progressive challenges across 5 worlds** — from CrashLoopBackOff to multi-failure chaos scenarios.

No cloud. No AWS. No costs. Real Kubernetes. Real debugging.

## Key Capabilities

- 🔍 **Runtime Fault Isolation** — Diagnose complex failures: `CrashLoopBackOff`, `ImagePullBackOff`, failed health probes, pending PVCs, and DNS resolution breakdowns
- 🛡️ **Multi-Tenant Cluster Governance** — Enforce RBAC policies, `SecurityContexts`, `NetworkPolicies`, and `ResourceQuotas` across namespaces
- ⚡ **Automated Traffic Scaling** — Configure and debug Horizontal Pod Autoscaling (HPA) with metrics-server integration
- 📜 **Declarative Remediation Manifests** — Author Kubernetes YAML fixes alongside automated Bash/Python validation scripts for reproducible runbooks
- 🔄 **Zero-Downtime Rollback Patterns** — Practice rolling updates, blue-green deployments, canary releases, and `PodDisruptionBudget` strategies
- 📊 **Real-time Cluster Monitoring** — Watch Kubernetes resources update live with the `check` command and `cgroup` metrics
- 💡 **Progressive Hint System** — Unlocks gradually as you investigate, mirroring real incident escalation
- 📚 **Post-Incident Debriefs** — Learn WHY your fix worked with production incident examples and interview prep
- 🎮 **Multi-Terminal Workflow** — Practice real-world debugging patterns across game + kubectl terminals
- 💾 **Auto-Save Progress** — Track your incident response journey with persistent XP and achievements

## 🛡️ Safety First

KubeRescue includes **comprehensive safety guards** (enabled by default):
- ✅ Prevents deletion of critical namespaces (kube-system, default, etc.)
- ✅ Blocks destructive cluster-wide operations
- ✅ Limits operations to `kuberescue` namespace via RBAC
- ✅ Confirms risky operations before execution
- ✅ Safe for beginners - hard to break things!

[Learn more about safety guards →](docs/SAFETY.md)

## Requirements
- Docker Desktop (running)
- kubectl
- kind
- bash
- python3 (3.9+)
- jq

## Platform Support

KubeRescue works on **Linux, macOS, and Windows**!

- ✅ **Linux** - Native bash support
- ✅ **macOS** - Native bash support  
- ✅ **Windows** - Requires Git Bash (see Windows installation below)

## Installation

### Linux & macOS

Quick setup - just run:
```bash
./install.sh
```

### Windows Installation

KubeRescue supports Windows! Follow these steps:

#### Prerequisites

1. **Docker Desktop** - [Download](https://www.docker.com/products/docker-desktop/)
   - Install and enable WSL2 backend (recommended)
   - **Start Docker Desktop** before running KubeRescue

2. **Git for Windows** - [Download](https://git-scm.com/download/win)
   - ✅ Includes Git Bash (required!)
   - ✅ Includes essential Unix utilities
   - **Important:** Always use Git Bash, not PowerShell or CMD

3. **kubectl** - Choose one installation method:
   ```bash
   # Option 1: Using Chocolatey (in PowerShell as Admin)
   choco install kubernetes-cli
   
   # Option 2: Using Scoop
   scoop install kubectl
   
   # Option 3: Manual download
   # Visit: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/
   ```

4. **Kind** - Choose one installation method:
   ```bash
   # Option 1: Using Chocolatey (in PowerShell as Admin)
   choco install kind
   
   # Option 2: Using Scoop
   scoop install kind
   
   # Option 3: Using Go (if you have Go installed)
   go install sigs.k8s.io/kind@latest
   ```

5. **Python 3.9+**
   - **Recommended:** Microsoft Store (search "Python 3.11" or newer)
   - Or download from [python.org](https://www.python.org/downloads/windows/)

6. **jq** ( Required for advanced )
   ```bash
   # Option 1: Using Chocolatey
   choco install jq
   
   # Option 2: Using Scoop
   scoop install jq
   ```

#### Running on Windows

⚠️ **CRITICAL:** Always use **Git Bash**, not PowerShell or CMD!

```bash
# 1. Open Git Bash (not PowerShell/CMD!)
# 2. Clone the repository
git clone https://github.com/kamesh-rautiya/KubeRescue.git
cd KubeRescue

# 3. Run installation
./install.sh

# 4. Start playing
./play.sh
```

#### Windows Troubleshooting

**Issue:** `TypeError: 'type' object is not subscriptable` when running `./play.sh`
- **Cause:** Python 3.8 or older is being used. KubeRescue requires **Python 3.9+**
- **Solution (macOS):**
  ```bash
  brew install python@3.11
  ./install.sh
  ```
- **Solution (Linux):**
  ```bash
  sudo apt install python3.11
  sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
  ./install.sh
  ```
- **Solution (Windows):** Install Python 3.11+ from Microsoft Store or [python.org](https://www.python.org/downloads/windows/)

**Issue:** `bash: command not found`
- **Solution:** Make sure you're using Git Bash, not PowerShell or CMD

**Issue:** `docker: command not found`  
- **Solution:** Start Docker Desktop and wait until it's fully running

**Issue:** Scripts show `^M` errors  
- **Solution:** This is fixed by `.gitattributes`, but if you still see it:
  ```bash
  git config core.autocrlf input
  git rm --cached -r .
  git reset --hard
  ```
#### Alternative: WSL2

For the best experience on Windows, use Windows Subsystem for Linux:

```bash
# In PowerShell (as Administrator)
wsl --install -d Ubuntu

# Then restart your computer and use Ubuntu terminal for KubeRescue
```

This provides a native Linux environment and the smoothest experience.

## Quick Start
```bash
# One-time setup
./install.sh

# Start playing
./play.sh
```

## 🎮 How to Play

1. **Start the game** - Run `./play.sh` (keeps the game running)
2. **Read the mission briefing** - Understand what's broken  
3. **OPEN A NEW TERMINAL** ⚠️ - Keep the game running in the first terminal!
4. **Use kubectl to investigate** - Check pods, logs, and events in the NEW terminal
5. **Fix the issue** - Apply corrections using kubectl commands
6. **Return to game terminal** - Choose an action (check/validate/guide)
7. **Earn XP** - Complete missions to level up!

## 🎯 Available Commands During Play

- `check` - Monitor resource status in real-time (watch for changes!)
- `guide` - Show step-by-step solution walkthrough *(Coming soon - will be updated in future)*
- `hints` - Display progressive hints (unlocks more on each use)
- `solution` - View the solution.yaml file
- `validate` - Test if your solution works
- `skip` - Skip to the next level (no XP awarded)
- `quit` - Exit the game (progress is auto-saved)

## 🎓 Post-Mission Debriefs

After completing each mission, you'll get a detailed debrief explaining:
- ✅ What actually happened and why
- 🧠 The correct mental model for this concept
- 🚨 Real-world production incident examples
- 💼 Interview questions you can now answer
- 🔧 kubectl commands you mastered

**This is where the real learning happens!**

## 🔧 Reset Levels

Get stuck or want to retry? Reset any level from any world:
```bash
# First, activate the virtual environment
source venv/bin/activate

# Reset levels from any world
python3 engine/reset.py level-1-pods                # World 1
python3 engine/reset.py level-15-rollout            # World 2
python3 engine/reset.py level-28-endpoints          # World 3
python3 engine/reset.py level-38-volume-permissions # World 4
python3 engine/reset.py level-45-node-affinity      # World 5
```

Or reset everything:
```bash
python3 engine/reset.py all
```

## 📚 Incident Debugging Path

### 🎯 World 1: Pod Lifecycle & Runtime Fault Isolation (Levels 1-10) 
**Difficulty**: Beginner | **Total XP**: 1,000  
Isolate and diagnose runtime faults using `kubectl`, container inspection, and Linux system internals.

- ✅ Level 1: CrashLoopBackOff — Bad container command diagnosis (100 XP)
- ✅ Level 2: Deployment Zero Replicas — Scaling failure isolation (100 XP)
- ✅ Level 3: ImagePullBackOff — Container image resolution debugging (100 XP)
- ✅ Level 4: Pending Pod — Scheduler constraint analysis (100 XP)
- ✅ Level 5: Labels & Selectors — Service-to-pod connectivity fault (100 XP)
- ✅ Level 6: Port Mismatch — Container networking misconfiguration (100 XP)
- ✅ Level 7: Multi-Container — Sidecar failure isolation (100 XP)
- ✅ Level 8: Pod Logs — Log-based incident triage (100 XP)
- ✅ Level 9: Init Container — Startup dependency deadlock (100 XP)
- ✅ Level 10: Namespace — Cross-namespace resource resolution (100 XP)

### 🏆 World 2: Deployment Strategies & Zero-Downtime Rollbacks (Levels 11-20) 
**Difficulty**: Intermediate | **Total XP**: 1,350  
Master zero-downtime rollback patterns, health probe debugging, and HPA autoscaling.

- ✅ Rolling updates, rollbacks, and declarative remediation manifests
- ✅ Liveness/readiness probe failures — health check diagnosis
- ✅ HPA autoscaling with metrics-server and cgroup metrics
- ✅ PodDisruptionBudgets, canary deployments, blue-green rollouts
- ✅ StatefulSets, ReplicaSets, and production lifecycle patterns

### 🏆 World 3: DNS Resolution & CNI/Networking Failures (Levels 21-30) 
**Difficulty**: Intermediate | **Total XP**: 2,100  
Systematically troubleshoot DNS resolution, service discovery, and NetworkPolicy enforcement.

- ✅ ClusterIP, NodePort, LoadBalancer — service type debugging
- ✅ CoreDNS resolution failures — FQDN and DNS policy diagnosis
- ✅ NetworkPolicy enforcement — ingress/egress traffic isolation
- ✅ Session affinity, cross-namespace communication, headless services
- ✅ Endpoint debugging and load balancer configuration

### 🏆 World 4: Storage Failures & Persistent Volume Debugging (Levels 31-40) 
**Difficulty**: Advanced | **Total XP**: 2,600  
Debug pending PVCs, access mode conflicts, StorageClass issues, and volume permission faults.

- ✅ PVC Pending — StorageClass and provisioner diagnosis
- ✅ Volume mount failures, access mode conflicts, reclaim policies
- ✅ StatefulSet volume management and persistent data lifecycle
- ✅ ConfigMap/Secret encoding errors and mount debugging
- ✅ Volume permissions and emptyDir vs PVC tradeoffs

### 🏆 World 5: Multi-Tenant Governance & Chaos Engineering (Levels 41-50) 
**Difficulty**: Advanced | **Total XP**: 3,150  
Harden multi-tenant cluster governance: RBAC policies, SecurityContexts, NetworkPolicies, and automated scaling.

- ✅ RBAC — ServiceAccount, Role, RoleBinding permission debugging
- ✅ SecurityContext — Pod Security Standards enforcement (restricted)
- ✅ ResourceQuotas — Namespace resource limit governance
- ✅ Taints/Tolerations, Node Affinity — scheduler constraint debugging
- ✅ PodDisruptionBudgets, PriorityClass — availability governance
- ✅ **Level 50**: 🔥 **The Chaos Finale** — 9 simultaneous production failures, end-to-end incident response

**Total Journey**: 50 Simulated Outages | 10,200 XP | Beginner → Kubernetes Incident Responder 🏆

📖 **Full Blueprint**: See [docs/50-CHALLENGE-BLUEPRINT.md](docs/50-CHALLENGE-BLUEPRINT.md) for detailed descriptions of all 50 challenges.

## 🔧 Technical Stack

| Component | Technology |
|-----------|-----------|
| **Cluster Runtime** | Kind (Docker), k3s |
| **CLI Tooling** | kubectl, jq, bash |
| **Validation Engine** | Bash/Python automated scripts |
| **Game Engine** | Python 3.9+ (Rich TUI framework) |
| **Manifests** | Declarative Kubernetes YAML |
| **Platform** | Linux, macOS, Windows (Git Bash) |



## 🛠️ Manual Play (Advanced)

If you prefer the old-school bash script:
```bash
./engine/start_game.sh
```

## 👨‍💻 Author

**Kamesh Rautiya**
- GitHub: [@kamesh-rautiya](https://github.com/kamesh-rautiya)
- Focus: Kubernetes Cluster Reliability, Cloud Native Incident Response, Chaos Engineering

## 📄 License

This project is licensed under the Apache 2.0 License - see the [License](License) file for details.

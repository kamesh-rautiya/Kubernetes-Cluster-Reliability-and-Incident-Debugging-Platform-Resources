#!/bin/bash
set -e

echo "🛡️  Setting up KubeRescue Safety Guards"
echo "======================================"
echo ""

# Check if kuberescue namespace exists
if ! kubectl get namespace kuberescue >/dev/null 2>&1; then
  echo "Creating kuberescue namespace..."
  kubectl create namespace kuberescue
fi

# Apply RBAC configuration
echo "Applying RBAC policies..."
kubectl apply -f rbac/kuberescue-rbac.yaml

echo ""
echo "✅ RBAC Setup Complete!"
echo ""
echo "📋 What was configured:"
echo "  • ServiceAccount: kuberescue-player"
echo "  • Role: Full access within kuberescue namespace"
echo "  • ClusterRole: Read-only cluster-wide access"
echo ""
echo "🔒 Safety Features:"
echo "  ✓ Cannot modify resources outside kuberescue namespace"
echo "  ✓ Cannot delete nodes or critical namespaces"
echo "  ✓ Cannot modify cluster-level resources"
echo "  ✓ Read-only access to cluster info (nodes, storage classes)"
echo ""
echo "💡 To use this ServiceAccount:"
echo "   kubectl --as=system:serviceaccount:kuberescue:kuberescue-player <command>"
echo ""
echo "Or configure your context to use it by default."
echo ""

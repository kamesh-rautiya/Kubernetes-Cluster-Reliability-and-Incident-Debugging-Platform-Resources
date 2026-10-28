#!/bin/bash

echo "🔍 Checking resource namespaces..."

# Check if resources exist in kuberescue namespace
POD_EXISTS=$(kubectl get pod client-app -n kuberescue 2>/dev/null)
SERVICE_EXISTS=$(kubectl get service backend-service -n kuberescue 2>/dev/null)

# Check if they're in wrong namespace
POD_IN_DEFAULT=$(kubectl get pod client-app -n default 2>/dev/null)
SERVICE_IN_DEFAULT=$(kubectl get service backend-service -n default 2>/dev/null)

if [[ -n "$POD_EXISTS" ]] && [[ -n "$SERVICE_EXISTS" ]]; then
    echo "   Pod: ✅ Found in kuberescue namespace"
    echo "   Service: ✅ Found in kuberescue namespace"
    echo "✅ Resources correctly deployed to kuberescue namespace"
    exit 0
else
    echo "❌ Resources not found in kuberescue namespace"
    if [[ -n "$POD_IN_DEFAULT" ]] || [[ -n "$SERVICE_IN_DEFAULT" ]]; then
        echo "💡 Found resources in 'default' namespace - they should be in 'kuberescue'"
    fi
    echo "💡 Check: kubectl get all -n kuberescue"
    echo "💡 Check: kubectl get all -n default"
    exit 1
fi

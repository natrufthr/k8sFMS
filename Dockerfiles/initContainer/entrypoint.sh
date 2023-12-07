#!/bin/sh

# Set SA_NAMESPACE to the namespace of the service account
SA_NAMESPACE=$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace)
export SA_NAMESPACE

# Set SA_TOKEN to the value of the service account token
SA_TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
export SA_TOKEN

# Set the Kubernetes cluster configuration
kubectl config set-cluster default-cluster --server=https://kubernetes.default --certificate-authority=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
kubectl config set-context default-context --cluster=default-cluster --user=default-user --namespace=${SA_NAMESPACE}
kubectl config set-credentials default-user --token=${SA_TOKEN}
kubectl config use-context default-context
kubectl config view --raw > /app/data/config.yaml

# Your main command goes here
exec "$@"

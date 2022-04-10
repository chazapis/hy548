# CRD example in minikube

This is an example showcasing custom resources in Kubernetes. We also build a very simple controller to work on the new CustomResourceDefinition.

## Setup

Start minikube, setup, and create the CRD:
```
minikube start --kubernetes-version=1.22.4
kubectl apply -f greeting-crd.yaml
```

Setup the environment for the controller:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Basic usage

Apply the custom resources:
```
kubectl apply -f hello-world.yaml
```

Now you can query them with:
```
kubectl get greetings
```

And manage them like any other Kubernetes resource:
```
kubectl delete greeting hello-world
kubectl delete greeting hello-to-all
```

## Controller

Start the controller (within the Python environment):
```
./controller.py
```

When you add a new "greeting", the controller should start a service. Removing a greeting will result in removing the corresponding service.

## Useful links

* Custom resources: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/

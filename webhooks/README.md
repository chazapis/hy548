# Webhook example in minikube

This is an example of a mutating webhook for Kubernetes.

## Setup

Start minikube and install [cert-manager](https://cert-manager.io):
```
minikube start --kubernetes-version=1.22.4
helm repo add jetstack https://charts.jetstack.io
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.7.2 --set installCRDs=true
```

Setup the environment for the webhook:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Basic usage

Get your local IP, replace it in where `192.168.1.1` is mentioned in `webhook.yaml`, and apply:
```
IP_ADDRESS=10.0.0.1
sed "s/192.168.1.1/${IP_ADDRESS}/" webhook.yaml | kubectl apply -f -
```

This will create the `custom-label-injector` namespace and a mutating webhook proxy that will forward all requests locally.

Start the controller (within the Python environment):
```
./controller.py
```

Create a new namespace with the appropriate label:
```
kubectl create namespace test
kubectl label namespace test custom-label-injector=enabled
```

Deploy a sample pod in the default namespace and in the new namespace and then get their labels.

You can also get all pods labeled with:
```
kubectl get pods -A --selector "custom-label"
```

## Useful links

* Webhooks: https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/

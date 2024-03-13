# Serverless example in minikube

This is an example on how to run serverless functions using [Fission](https://fission.io) in Kubernetes.

## Setup

Start minikube, setup and install software with [Helm](https://helm.sh):
```
minikube start --kubernetes-version=1.28.3
minikube addons enable ingress
minikube addons enable metrics-server

# Install Locust (https://artifacthub.io/packages/helm/deliveryhero/locust)
helm repo add deliveryhero https://charts.deliveryhero.io/
kubectl create configmap my-loadtest-locustfile --from-file "$PWD/locustfiles/main.py"
kubectl create configmap my-loadtest-lib --from-file "$PWD/locustfiles/lib/"
helm install locust deliveryhero/locust --version 0.26.1 \
  --set ingress.enabled=true \
  --set ingress.hosts\[0\].host="locust.localtest.me" \
  --set ingress.hosts\[0\].path="/" \
  --set ingress.hosts\[0\].pathType="ImplementationSpecific" \
  --set loadtest.name=my-loadtest \
  --set loadtest.locust_locustfile_configmap=my-loadtest-locustfile \
  --set loadtest.locust_lib_configmap=my-loadtest-lib

# Install Fission (https://artifacthub.io/packages/helm/fission-charts/fission-all)
kubectl create namespace fission
kubectl create -k "github.com/fission/fission/crds/v1?ref=v1.15.1"
helm repo add fission-charts https://fission.github.io/fission-charts/
helm install fission fission-charts/fission-all --version v1.15.1 --namespace fission \
  --set routerServiceType=NodePort
```

On a terminal:
```
minikube tunnel
```

On another terminal:
```
minikube dashboard
```

You can also monitor the CPU usage inside minikube with:
```
minikube ssh top
```

You can change the metrics resolution by running the following, and setting `--metric-resolution=10s` in the container args:
```
kubectl -n kube-system edit deployments.apps metrics-server
```

## Basic usage

Add a "hello world" function in Fission:
```
fission env create --name python --image fission/python-env
fission function create --name hello-py --env python --code hello.py
fission function test --name hello-py
```

Add function to a route:
```
fission route create --name hello --url /hello --function hello-py --createingress --ingressrule "fission.localtest.me=/hello"
```

Verify the application is working, by visiting http://fission.localtest.me/hello.

Open Locust at http://locust.localtest.me. Enter `http://router.fission.svc` in the "host" box and then click on "Start swarming". Select the "Charts" tab to see the graphs in real time.

Try with a different number of users (concurrency) etc.

Monitor the usage through `top` inside minikube, from the dashboard, or by running:
```
kubectl top pod
```

Remove the function with:
```
fission route delete --name hello
fission function delete --name hello-py
fission env delete --name python
```

## Autoscaling

Add the same function with the "newdeploy" executor type:
```
fission env create --name python --image fission/python-env
fission fn create --name hello-py --env python --code hello.py --executortype newdeploy \
  --minscale 1 --maxscale 8 --maxcpu 200 --maxmemory 256
fission route create --name hello --url /hello --function hello-py --createingress --ingressrule "fission.localtest.me=/hello"
```

Run the tests again.

You can also monitor HPA updates with:
```
kubectl get hpa -n fission-function --watch
```

## Useful links

* Helm cheat sheet: https://phoenixnap.com/kb/helm-commands-cheat-sheet
* Fission autoscaling: https://fission.io/docs/usage/function/executor/
* Enabling and using metrics in minikube: http://www.mtitek.com/tutorials/kubernetes/kubernetes_metrics.php
* Changing the metrics resolution: https://vahid4m.medium.com/change-metric-resolution-interval-on-minikube-1033ffb74e05
* If CPU usage is not shown: https://github.com/kubernetes/minikube/issues/13620

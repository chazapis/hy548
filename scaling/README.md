# HPA example in minikube

This is an example on how manual and automatic scaling (using the HorizontalPodAutoscaler) works in Kubernetes.

## Setup

Start minikube, setup and create the resources:
```
minikube start --kubernetes-version=1.28.3
minikube addons enable ingress
minikube addons enable metrics-server
kubectl apply -f flask.yaml
kubectl apply -f locust.yaml
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

Verify the application is working, by visiting http://127.0.0.1/hello.

Open Locust at http://127.0.0.1.

Get your minikube IP with:
```
minikube ip
```

This is the external address that we will tell Locust to test. Enter it in the "host" box as `http://<IP address>`, and then click on "Start swarming". Select the "Charts" tab to see the graphs in real time.

Scale up the deployment with:
```
kubectl scale deployments/flask --replicas=2
```

Scale down, try with a different number of users (concurrency) etc.

Monitor the usage through `top` inside minikube, from the dashboard, or by running:
```
kubectl top pod
```

## Autoscaling

Scale the deployment down to one replica and enable the HPA with:
```
kubectl autoscale deployment flask --cpu-percent=20 --min=1 --max=8
```

Run the tests again.

You can also monitor HPA updates with:
```
kubectl get hpa --watch
```

## Useful links

* Running Locust in Docker: http://docs.locust.io/en/stable/running-in-docker.html
* HPA basics: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
* Enabling and using metrics in minikube: http://www.mtitek.com/tutorials/kubernetes/kubernetes_metrics.php
* Changing the metrics resolution: https://vahid4m.medium.com/change-metric-resolution-interval-on-minikube-1033ffb74e05
* If CPU usage is not shown: https://github.com/kubernetes/minikube/issues/13620

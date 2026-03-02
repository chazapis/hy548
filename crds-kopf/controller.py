#!/usr/bin/env python

import kopf
import yaml

from kubernetes import client, config
from jinja2 import Template

SERVICE_TEMPLATE = '''
apiVersion: v1
kind: Service
metadata:
  name: {{ name }}
  labels:
    created-by: greetings-controller
spec:
  type: ClusterIP
  ports:
  - port: 8080
  selector:
    app: {{ name }}
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ name }}
spec:
  replicas: {{ replicas }}
  selector:
    matchLabels:
      app: {{ name }}
  template:
    metadata:
      labels:
        app: {{ name }}
    spec:
      containers:
      - name: hello-kubernetes
        image: carvicsforth/hello-kubernetes:1.10
        env:
        - name: MESSAGE
          value: {{ message }}
'''

@kopf.on.create('greetings')
def create_fn(spec, name, namespace, logger, **kwargs):
    logger.info('Object %s created in namespace %s.', name, namespace)

    # Render the pod yaml with some spec fields used in the template.
    logger.info('Rendering template...')
    rendered_template = Template(SERVICE_TEMPLATE).render(name=name, message=spec.get('message', 'Greetings!'), replicas=spec.get('replicas', 1))

    # Actually create an object by requesting the Kubernetes API.
    try:
        config.load_kube_config()
    except:
        config.load_incluster_config()

    core_v1 = client.CoreV1Api()
    apps_v1 = client.AppsV1Api()

    documents = list(yaml.safe_load_all(rendered_template))
    for doc in documents:
        # Make it our child: assign the namespace, name, labels, owner references, etc.
        kopf.adopt(doc)

        kind = doc["kind"]
        if kind == "Service":
            core_v1.create_namespaced_service(namespace, body=doc)
            logger.info('Service created.')
        elif kind == "Deployment":
            apps_v1.create_namespaced_deployment(namespace, body=doc)
            logger.info('Deployment created.')

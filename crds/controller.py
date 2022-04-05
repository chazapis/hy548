#!/usr/bin/env python

import os
import logging

from time import sleep
from jinja2 import Template

from kubeclient import KubeClient

kubeclient = KubeClient()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

SERVICE_DIRECTORY = os.path.join(os.getcwd(), 'tmp')
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
        image: paulbouwer/hello-kubernetes:1.10
        env:
        - name: MESSAGE
          value: {{ message }}
'''

def create_service(name, message, replicas):
    filename = os.path.join(SERVICE_DIRECTORY, '%s.yaml' % name)
    if os.path.exists(filename):
        logging.warning('Service file already exists. Skipping...')

    logging.info('Writing rendered template in %s and creating service...' % filename)
    rendered_template = Template(SERVICE_TEMPLATE).render(name=name, message=message, replicas=replicas)
    with open(filename, 'w') as f:
        f.write(rendered_template)
    kubeclient.apply_yaml_file(filename)

def delete_service(name):
    filename = os.path.join(SERVICE_DIRECTORY, '%s.yaml' % name)
    if not os.path.exists(filename):
        logging.warning('Service file not found. Skipping...')

    logging.info('Removing service %s and associated rendered template...' % filename)
    kubeclient.delete_yaml_file(filename)
    os.unlink(filename)

def check_and_apply():
    logging.info('New loop')
    namespaces = [n.metadata.name for n in kubeclient.list_namespaces()]
    for namespace in namespaces:
        logging.info('Working in namespace: %s' % namespace)

        greetings = kubeclient.list_crds(group='hy548.csd.uoc.gr', version='v1', namespace=namespace, plural='greetings')
        services = [s.metadata.name for s in kubeclient.list_services(namespace=namespace, label_selector='created-by==greetings-controller')]

        for greeting in greetings:
            name = greeting['metadata']['name']
            message = greeting['spec']['message']
            replicas = greeting['spec']['replicas']
            logging.info('Found crd: %s (message: %s, replicas: %s)' % (name, message, replicas))

            if name in services:
                services.remove(name)
                logging.info('Service already created. Skipping...')
                continue

            create_service(name, message, replicas)

        for service in services:
            delete_service(service)

if __name__ == '__main__':
    if not os.path.exists(SERVICE_DIRECTORY):
        os.makedirs(SERVICE_DIRECTORY)

    try:
        while True:
            check_and_apply()
            sleep(3)
    except KeyboardInterrupt:
        pass

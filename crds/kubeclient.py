# Copyright [2019] [FORTH-ICS]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Trimmed down version of kubernetes.py from Karvdash (https://github.com/CARV-ICS-FORTH/karvdash).

import os

import kubernetes.client
import kubernetes.config
import kubernetes.stream

class KubeClient(object):
    def __init__(self):
        self._config_loaded = False
        self._core_client = None
        self._custom_objects_client = None

    def _load_config(self):
        if self._config_loaded:
            return
        try:
            kubernetes.config.load_kube_config()
        except:
            kubernetes.config.load_incluster_config()
        self._config_loaded = True

    @property
    def core_client(self):
        if not self._core_client:
            self._load_config()
            self._core_client = kubernetes.client.CoreV1Api()
        return self._core_client

    @property
    def custom_objects_client(self):
        if not self._custom_objects_client:
            self._load_config()
            self._custom_objects_client = kubernetes.client.CustomObjectsApi()
        return self._custom_objects_client

    def list_namespaces(self):
        return self.core_client.list_namespace().items

    def list_services(self, namespace, label_selector):
        return self.core_client.list_namespaced_service(namespace=namespace, label_selector=label_selector).items

    def list_crds(self, group, version, namespace, plural):
        return self.custom_objects_client.list_namespaced_custom_object(group=group, version=version, namespace=namespace, plural=plural)['items']

    def apply_yaml_file(self, yaml_file, namespace=None):
        command = 'kubectl apply -f \'%s\'' % yaml_file
        if namespace:
            command += ' -n %s' % namespace
        os.system(command)

    def delete_yaml_file(self, yaml_file, namespace=None):
        command = 'kubectl delete -f \'%s\'' % yaml_file
        if namespace:
            command += ' -n %s' % namespace
        os.system(command)

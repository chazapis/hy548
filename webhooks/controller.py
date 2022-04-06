#!/usr/bin/env python

import jsonpatch
import copy
import base64
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

def inject_label(yaml_data, label):
    for part in yaml_data:
        if 'labels' not in part['metadata']:
            part['metadata']['labels'] = {}
        part['metadata']['labels'][label] = 'true'

@app.route('/mutate', methods=['POST'])
def mutate():
    data = request.get_json()
    uid = data['request']['uid']
    service = copy.deepcopy(data['request']['object'])
    inject_label([service], os.getenv('CUSTOM_LABEL', 'custom-label'))
    patch = jsonpatch.JsonPatch.from_diff(data['request']['object'], service)
    encoded_patch = base64.b64encode(patch.to_string().encode('utf-8')).decode('utf-8')

    return jsonify({'apiVersion': 'admission.k8s.io/v1',
                   'kind': 'AdmissionReview',
                   'response': {'uid': uid,
                                'allowed': True,
                                'status': {'message': 'Adding extra label'},
                                'patchType': 'JSONPatch',
                                'patch': encoded_patch}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

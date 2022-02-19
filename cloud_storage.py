from os import name
import cloudsync as cs
import tempfile as tf
import pandas as pd
import json
from config import check_config 

credsPath = check_config()

def connect(credsPath):
    oauth_config = cs.command.utils.generic_oauth_config('onedrive')
    provider = cs.create_provider('onedrive', oauth_config=oauth_config)
    f = open(credsPath, 'r')
    creds = json.load(f)
    provider.connect(creds)
    return provider

def change_namespace(path_in_ns, provider, namespace=None):
    # Change namespace to shared folder
    ns = provider.list_ns()
    if namespace is None:
        shared_folder_name = path_in_ns
        for x in ns:
            if shared_folder_name in x.name:
                break
        print("Changing namespace to: {}".format(x.id))
        provider.namespace = x
    else:
        for x in ns:
            if namespace in x.name:
                break
        print("Changing namespace to: {}".format(x.id))
        provider.namespace = x

def download_file(filename, provider, namespace=None, output=None):
    if not namespace is None:
        change_namespace(namespace)
    if output is None:
        tmp = tf.NamedTemporaryFile()
        print("Downloading to {} ...".format(tmp.name))
    else:
        tmp = open(output, 'w')
    provider.download_path(filename, tmp)
    tmp.seek(0) # Go back to first line
    return tmp

def upload_file():
    print("> upload_file()")
    print("Still to be implemented...")
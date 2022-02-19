from os import name
import cloudsync as cs
import tempfile as tf
import pandas as pd
import json

def connect():
    oauth_config = cs.command.utils.generic_oauth_config('onedrive')
    provider = cs.create_provider('onedrive', oauth_config=oauth_config)
    f = open('creds.json', 'r')
    creds = json.load(f)
    provider.connect(creds)
    return provider, creds

# "global" variables
provider, __creds__ = connect()

def check_connection(self):
    pass

def change_namespace(self, path_in_ns, namespace=None):
    # Change namespace to shared folder
    ns = self.provider.list_ns()
    if namespace is None:
        shared_folder_name = path_in_ns
        for x in ns:
            if shared_folder_name in x.name:
                break
        print("Changing namespace to: {}".format(x.id))
        self.provider.namespace = x
    else:
        for x in ns:
            if namespace in x.name:
                break
        print("Changing namespace to: {}".format(x.id))
        self.provider.namespace = x

def download_file(self, filename, namespace=None, output=None):
    if not namespace is None:
        self.change_namespace(namespace)
    if output is None:
        tmp = tf.TemporaryFile()
    else:
        tmp = open(output, 'w')
    self.provider.download_path(filename, tmp)
    tmp.seek(0) # Go back to first line
    return tmp

def upload_file():
    print("upload file")
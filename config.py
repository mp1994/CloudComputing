import cloudsync as cs
import json
import os
from os.path import exists

def get_auth_token():
    oauth_config = cs.command.utils.generic_oauth_config('onedrive')
    provider = cs.create_provider('onedrive', oauth_config=oauth_config)
    creds = provider.authenticate()
    return creds

def save_auth_token(fname="$HOME/.creds.json", creds=None):
    f = open(fname, 'w')
    json.dump(creds, f)

def check_config():
    defaultPath = os.environ['HOME'] + "/.creds.json"
    if exists(defaultPath):
        print("Configuration found in: {}".format(defaultPath))
        return defaultPath
    else:
        print("No configuration found in default path.")

def config():
    print("Starting OneDrive auth...")
    token = get_auth_token()
    defaultPath = os.environ['HOME'] + "/"
    print("Specify path to save OneDrive auth token ({}): ".format(defaultPath), end='')
    f = input()
    if len(f) == 0:
        f = defaultPath
    f = f + ".creds.json"
    save_auth_token(f, creds=token)
    print("Token saved to file: {}".format(f))
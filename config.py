import cloudsync as cs
import json
import os
from os.path import exists
import subprocess

def get_auth_token():
    oauth_config = cs.command.utils.generic_oauth_config('onedrive')
    provider = cs.create_provider('onedrive', oauth_config=oauth_config)
    creds = provider.authenticate()
    return creds

def save_auth_token(fname="$HOME/.creds.json", creds=None):
    f = open(fname, 'w')
    json.dump(creds, f)

def check_config(silent=False):
    defaultPath = os.environ['HOME'] + "/.creds.json"
    if exists(defaultPath):
        if not silent:
            print("[INFO] Configuration found in: {}".format(defaultPath))
        return defaultPath
    else:
        if not silent:
            print("[INFO] No configuration found in default path.")
        return False

def config(Force=False):
    # cloud_storage
    if check_config() == False:
        print("Starting OneDrive auth...")
    else:
        if Force == False:
            print("Use check_config(Force=True) to overwrite existing configuration.")
            return
    token = get_auth_token()
    defaultPath = os.environ['HOME'] + "/"
    print("Specify path to save OneDrive auth token ({}): ".format(defaultPath), end='')
    f = input()
    if len(f) == 0:
        f = defaultPath
    f = f + ".creds.json"
    save_auth_token(f, creds=token)
    print("[INFO] Token saved to file: {}".format(f))
    # SSH
    defaultPath = os.environ['HOME'] + "/." + os.environ['USER'] + "-config.ini"
    if exists(defaultPath):
        print("[INFO] Global SSH configuration found in {}".format(defaultPath))
    else:
        print("[WARNING] Global SSH configuration not found. Call config.make_config() to create one.")

def make_config(local=False):
    if local:
        defaultPath = "./config.ini"
    else:
        defaultPath = os.environ['HOME'] + "/." + os.environ['USER'] + "-config.ini"
        if exists(defaultPath):
            print("[INFO] Global configuration already set. This will overwrite the existing configuration.")
    host = input("SSH user@host: ")
    if not "@" in host:
        print("Please provide user and host (e.g., admin@127.0.0.1")
        return
    port = input("SSH port (22): ") or "22" # Default: 22
    f = open(defaultPath, 'w')
    if f.closed:
        print("[ERROR] Unable to open file {}".format(defaultPath))
        return
    f.write("[SSH]\n")
    f.write("host = {}\n".format(host))
    f.write("port = {}\n".format(port))
    f.close()
    print("[INFO] {} configuration saved successfully.".format("Local" if local else "Global"))

def check_ssh_connection(host=None, port=22):
    if host is None:
        print("[ERROR] The first input cannot be None: provide a username-host pair, such as: user@127.0.0.1")
        return
    cmd = "ssh -p {} {} uname -n".format(port, host)
    print("Testing connection: " + cmd)
    cmd = "ssh -p {} {} uname -n".format(port, host)
    try:
        out = subprocess.check_output(cmd, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        print("[WARNING] SSH connection issue.")
        return
    print("[INFO] Connected to host: {}".format(out))
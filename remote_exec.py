import os
import subprocess
import tempfile as tf
from vars import ssh_port, ssh_host

def remote_exec(path):
    print("Exec from: {}".format(path))
    # Open the calling script (from path) and read the file
    fin = open(path, 'r')
    # Split the script and take everything after separator
    s = fin.read().split("remote_exec(__file__)")[-1]
    # Write to file
    tmp = tf.NamedTemporaryFile(suffix=".py")
    fout = open(tmp.name, 'w')
    fout.write(s)
    fout.close()
    # Run over SSH
    subprocess.Popen("/usr/bin/ssh -p {} {} python3 -u - < {}".format(ssh_port, ssh_host, tmp.name), shell=True)
    # Exit to prevent the calling script to run locally
    exit(0)
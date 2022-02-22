import os
import subprocess
import tempfile as tf
import vars

def remote_exec(path):
    print("Exec from: {}".format(path))
    # Open the calling script (from path) and read the file
    fin = open(path, 'r')
    # Split the script and take everything after separator
    s = fin.read().split("remote_exec(__file__)")[-1]
    # Write to file
    tmp = os.path.join(tf.gettempdir(), os.urandom(8).hex() + '.py')
    fout = open(tmp, 'w')
    fout.write(s)
    fout.close()
    # Run over SSH
    print(vars.ssh_host + " " + vars.ssh_port)
    subprocess.Popen("/usr/bin/ssh -p {} {} python3 -u - < {}".format(vars.ssh_port, vars.ssh_host, tmp), shell=True)
    # Exit to prevent the calling script to run locally
    exit(0)
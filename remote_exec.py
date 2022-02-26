import os
import subprocess
import tempfile as tf
import vars

def remote_exec(path, verbose=True, logfile=None):
    # If localhost, return
    if 'localhost' in vars.ssh_host or '127.0.0.1' in vars.ssh_host:
        print("Running on local machine...")
        return
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
    cmd = "/usr/bin/ssh -p {} {} python3 -u - < {}".format(vars.ssh_port, vars.ssh_host, tmp)
    if not verbose:
        cmd = cmd + " 1>/dev/null 2>&1"
    if not logfile is None:
        print("Logging to file: {}".format(logfile))
        cmd = cmd + " > {}".format(logfile)
    subprocess.Popen(cmd, shell=True)
    # Exit to prevent the calling script to run locally
    exit(0)
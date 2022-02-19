import os
import subprocess
import tempfile as tf
DEBUG = False

def remote_exec(path):
    print("Exec from: {}".format(path))
    # Open calling script (from path) and read the file
    fin = open(path, 'r')
    # Split the script and take everything after separator
    s = fin.read().split("remote_exec(__file__)")[-1]
    # DEBUG: print script portion
    if DEBUG:
        print(s)
    # Write to file
    tmp = "foo.py" #tf.NamedTemporaryFile(suffix=".py")
    fout = open(tmp, 'w')
    print(fout.name)
    fout.write(s)
    fout.close()
    # Run over SSH
    subprocess.Popen("/usr/bin/ssh pesenti@10.75.4.93 python3 -u - < {}".format(fout.name), shell=True)
    # Exit to prevent calling script to run locally
    exit(0)
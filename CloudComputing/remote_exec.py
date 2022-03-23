import os
import subprocess
import tempfile as tf
from . import vars
from .config import get_token
from .cc_debug import cc_print

def remote_exec(path, rdir="./", verbose=True, logfile="nohup.out"):
    # If localhost, return
    if 'localhost' in vars.ssh_host or '127.0.0.1' in vars.ssh_host:
        cc_print("Running on local machine...", 2)
        return
    cc_print("[INFO] Running from file: {}".format(path), 1)
    # Open the calling script (from path) and read the file
    fin = open(path, 'r')
    # Split the script and take everything after separator
    s = fin.read().split("__file__")[-1]
    s = s[s.find("\n")+1:len(s)]   
    # Do we need to import CloudComputing? 
    if "CloudComputing" in s or "cc" in s:
        s = "import CloudComputing as cc\ncc.vars.token = {}\ncc.__token__ = cc.vars.token\ncc.connect()".format(get_token()) + s
    # Write to file
    tmp = os.path.join(tf.gettempdir(), os.urandom(8).hex() + '.py')
    fout = open(tmp, 'w')
    fout.write(s)
    fout.close()
    # CD to remote dir (if any)
    cmd = cmd = "nohup /usr/bin/ssh -p {} {}".format(vars.ssh_port, vars.ssh_host)
    cmd = cmd + " 'cd {} &&".format(rdir)
    # Copy the temp file (script) to the remote working dir
    xmd = "/usr/bin/scp -o LogLevel=Error -P {} {} {}:{}".format(vars.ssh_port, tmp, vars.ssh_host, rdir)
    subprocess.run(xmd, shell=True)
    # Run over SSH
    cmd = cmd + " python -u {}'".format(tmp.split("/")[-1]) # Remove "/tmp/" from the filename
    if not verbose:
        cmd = cmd + " 1>/dev/null 2>&1"
    if logfile != 'nohup.out':
        cc_print("Logging to file: {}".format(logfile), 1)
        cmd = cmd + " > {}".format(logfile)
    r = subprocess.Popen(cmd, shell=True)
    os.system('echo "" > nohup.out')
    os.system("tail -f {}".format(logfile))    
    # Now we can safely remove the local temp file
    subprocess.run("rm {}".format(tmp), shell=True)
    # Remove the remote temp file
    os.system("/usr/bin/ssh -p {} {} 'rm {}/{}'".format(vars.ssh_port, vars.ssh_host, rdir, tmp.split("/")[-1]))
    # Exit to prevent the calling script to run locally
    exit(0)
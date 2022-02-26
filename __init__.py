from cloud_storage import connect, change_namespace, download_file, upload_file
from config import config, check_config, check_ssh_connection, make_config, load_config
from remote_exec import remote_exec
import vars

# CloudComputing version
_version = "0.0.2"

## Global variables
# cloud_storage
vars.creds_path = check_config(silent=True)
creds = vars.creds_path
# remote_ssh
c = load_config()
vars.ssh_host = c['SSH']['host']
vars.ssh_port = c['SSH']['port']
print("{} {}".format(vars.ssh_host, vars.ssh_port))
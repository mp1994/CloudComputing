from cloud_storage import connect, change_namespace, download_file, upload_file
from config import config, check_config, check_ssh_connection
from remote_exec import remote_exec
import configparser
import vars

# CloudComputing version
_version = "0.0.2"

## Global variables
# cloud_storage
vars.creds_path = check_config(silent=True)
# remote_ssh
c = configparser.ConfigParser()
c.read("config.ini")
vars.ssh_host = c['SSH']['host']
vars.ssh_port = c['SSH']['port']
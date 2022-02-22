from cloud_storage import connect, change_namespace, download_file, upload_file
from config import config, check_config, check_ssh_connection
from remote_exec import remote_exec
import configparser
from vars import *

# CloudComputing version
_version = "0.0.2"

## Global variables
# cloud_storage
creds_path = check_config(silent=True)
# remote_ssh
c = configparser.ConfigParser()
c.read("config.ini")
ssh_host = c['SSH']['host']
ssh_port = c['SSH']['port']
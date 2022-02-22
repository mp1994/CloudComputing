from cloud_storage import connect, change_namespace, download_file, upload_file
from config import config, check_config, check_ssh_connection
from remote_exec import remote_exec

_version = "0.0.1"
__creds__ = check_config(silent=True)
credsPath = __creds__
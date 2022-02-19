from cloud_storage import connect, change_namespace, download_file, upload_file
from config import config, check_config
from remote_exec import remote_exec

__version__ = "0.0.1"
__creds__ = check_config()
credsPath = __creds__
provider = connect(credsPath)
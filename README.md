# CloudComputing for Python

The `CloudComputing` package can be used to easily exploit advanced functions such as remote executing over SSH and cloud storage (OneDrive/GDrive) with Python.
The remote execution (`remote_exec.py`) is handled over SSH: source files can be developed and maintained locally and then executed remotely over SSH.
Cloud storage is based on the Python package [cloudsync](https://pypi.org/project/cloudsync/), that supports both Google Drive and OneDrive. It allows to store large datasets on the cloud and access them both locally and remotely, combined with the `remote_exec` functionality. 

### Requirements

All the required Python packages are listed in the file `requirement.txt` and hence installed automatically with this package. `CloudComputing` was developed and tested on Python 3.9.6 on Linux. The `remote_exec` module is currently working only on Unix systems (by choice...)
You need to set up a secure shell (SSH) connection with the remote host for the `remote_exec` module before using this functionality. You may find instructions on how to do this on the web, such as [this one](https://medium.com/@SergioPietri/how-to-setup-and-use-ssh-for-remote-connections-e86556d804dd).
### Install

The install process should be straight-forward: `pip install CloudComputing`. I recommend using [pyenv](https://github.com/pyenv/pyenv).

### Configuration

The `cloud_storage` module is based on the PyPi package `cloudsync`. By default, the latter handles authentication wih OAuth and does not store user credentials, requiring re-authentication at every session. The `config` module provides functions to save and manage the OAuth token. This is saved in `json` format locally, either in `$HOME` (default) or in a user-provided path. Both OneDrive Personal and OneDrive for Business accounts should work out-of-the-box, with support for shared folders.

The `remote_exec` module can be configured either with a `config.ini` file, either globally (user space) or locally (project workspace). Please mind that the local configuration has higher priority over the global one, if any. This is intended to have both a user-defined default server and project-specific servers.
##### Global Configuration
The global configuration can be set either manually or calling the `config.make_config()` function:
```
$ python -c 'import CloudComputing as cc; cc.make_config()'
```
This will set the default `user@host` and the default `port` for SSH communication. The global configuration file is stored in `$HOME/.$USER-config.ini`.
##### Local Configuration
Any project may have its local configuration. Local configurations have higher priority. They are specified by means of a local `config.ini` in the project's path, with the following structure. Local configurations may be created also with `config.make_config(local=True)`
```
; config.ini
[SSH]
host = "user@127.0.0.1"
port = 22
```

### Example

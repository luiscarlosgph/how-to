Upload
------
* Upload a file or a set of files to synapse:


* Upload a folder and its contents to Synapse:


Download
--------
```
$ python3 -m synapseclient -u <synapse_username> -p <synapse_password> get -r "<synapse_id>"
```
If the **synapse_id** points to a directory, this command will download the contents of the directory into the current local directory.

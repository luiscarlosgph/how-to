Install synapseclient
---------------------
```
$ python3 -m pip install synapseclient
```

Upload
------
* Upload a file to Synapse:


* Upload a directory and its contents to Synapse:


Download
--------
* Download a file into the current local directory:
```
$ python3 -m synapseclient -u <synapse_username> -p <synapse_password> get <synapse_id>
```

* Download the contents of a Synapse directory into the current local directory:
```
$ python3 -m synapseclient -u <synapse_username> -p <synapse_password> get -r <synapse_id>
```

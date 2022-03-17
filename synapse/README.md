Install synapseclient
---------------------
```
$ python3 -m pip install synapseclient
```

Upload
------
Download the uploader script:
```
$ wget https://raw.githubusercontent.com/luiscarlosgph/how-to/main/synapse/synapse_uploader.py
```

* Upload a file or directory to Synapse:
```
$ python3 synapse_uploader.py --username <synapse_username> --password <synapse_password> --parent-id <synapse_id> --input-path <path_to_file_or_directory>
```

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

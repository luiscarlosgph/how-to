Use case
--------

You have a Python app that runs an HTTP server listening on a port in the loopback interface and is not able to deal with HTTPS requests (or malicious requests).

1. Install ngynx:
   ```bash
   $ sudo apt install nginx
   ```
 
 2. Choose the listening port for nginx modifying the `listen` instruction in `$ sudo vim /etc/nginx/sites-available/default`:
    ```
    listen 8080 default_server;
    listen [::]:8080 default_server;
    ```

3. Edit nginx configuration file via `$ sudo vim /etc/nginx/sites-available/default`, and modify the `location` instruction as follows:

   ```
   location / {
           proxy_pass http://localhost:12345;
   }
   ```
   
   This will redirect all the HTTP and HTTPS requests to the port `8080` of the host to `127.0.0.1:12345`.

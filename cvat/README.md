Description
-----------

[CVAT](https://opencv.github.io/cvat/about) is a popular web annotation tool.


Dependencies
------------

Install Docker following [these instructions](https://github.com/luiscarlosgph/how-to/tree/main/docker).


Setup CVAT
----------

1. Pull CVAT images and run containers: 

   ```
   $ git clone https://github.com/opencv/cvat
   $ cd cvat
   $ docker compose up -d
   ```
   
2. Create CVAT superuser:
   ```
   $ docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
   ```
   
   TODO: this command above is crashing

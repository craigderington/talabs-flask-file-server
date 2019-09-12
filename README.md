### Flask Web Server 
#### Serve static XML files from a Flask app

##### INSTALL

Clone this repository, create a new virtual environment and install dependencies.  

```
$ cd flask-file-server/
$ virtualenv .env --python=python3
$ (.env) pip3 install -r requirements.txt
$ (.env) gunicorn -b 0.0.0.0:8000 -w 2 wsgi:app
```

#### Docker

Alternatively, close this repository and build your Docker image.  

##### BUILD

To build this image...

```
$ docker build -t flask-file-server:latest .
```

##### RUN

Now run the new image as a container

```
$ docker run -ti -d -p 8000:8000 flask-file-server:latest
```




# Login Page with Python Flask Dockerized Application #

Build the image using the following command

```bash
docker build -t flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
docker run -d --name test -e db_ip=172.17.0.2 -p 8080:8080 --rm flask-app:latest 
```
or

```bash
docker run -d --name test -e db_ip=172.17.0.2 -e db_user=login db_pass=SecurePass -p 8080:8080 --rm flask-app:latest
```

The application will be accessible at http:X.X.X.X:8080.
You need to set 3 environnement variable db_ip, db_user and db_pass, default value see below.

db_ip=127.0.0.1
db_user=login
db_pass=123456

# K1S
- https://hub.docker.com/_/httpd


### Build & Run
```bash
$ docker build -t my-apache2     # build
$ docker run -dit --name my-running-app -p 8080:80 my-apache2    # run
$ docker exec -it my-running-app bash    # enter into container
-----
$ docker build -t blog docker/httpd
$ docker build -t lb docker/nginx
```

### LB
```
$ sudo docker run -d --name blog-1 --rm blog
$ sudo docker run -d --name blog-2 --rm blog
$ sudo docker run -d --name nginx_lb -p 80:80 --link blog-1:blog-1 --link blog-2:blog-2 lb
```

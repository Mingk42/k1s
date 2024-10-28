# K1S
- https://hub.docker.com/_/httpd


### Build & Run
```bash
$ docker build -t my-apache2     # build
$ docker run -dit --name my-running-app -p 8080:80 my-apache2    # run
$ docker exec -it my-running-app bash    # enter into container
```


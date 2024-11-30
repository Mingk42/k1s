FROM httpd:2.4

#WORKDIR 

COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf
ARG REPO_URL=https://github.com/Mingk42/Mingk42.github.io.git

RUN ["apt","update"]
RUN ["apt","install","vim","-y"]
RUN ["apt","install","git","-y"]
RUN git clone ${REPO_URL} /usr/local/apache2/blog/

#ENTRYPOINT

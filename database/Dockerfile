FROM mysql:5.7.22
RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/shigure37/El.git
RUN cp El/database/docker/db/*.sql /docker-entrypoint-initdb.d/
RUN chmod -R 775 /docker-entrypoint-initdb.d
RUN cp El/database/docker/conf/*.cnf /etc/mysql/
EXPOSE 3306
CMD ["mysqld"]

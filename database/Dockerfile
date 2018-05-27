FROM mysql:5.7.22
COPY docker/db/*.sql /docker-entrypoint-initdb.d/ 
RUN chmod -R 775 /docker-entrypoint-initdb.d/
COPY docker/conf/*.cnf /etc/mysql/
EXPOSE 3306
CMD ["mysqld"]


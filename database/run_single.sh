#!/bin/sh
docker run --name mysql_single -p 3306:3306 -e MYSQL_ROOT_PASSWORD=guoke618 stockdb:1.0

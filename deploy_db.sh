#!/bin/sh
command -v docker >/dev/null 2>&1 || { echo >&2 "not found docker, please install docker first."; exit 1; }
docker

#!/bin/bash
set -e

docker run -v thesis-build:/home/phd/build hertzsprung/thesis rm -rf /home/phd/build/{*,.*}
if [[ ! -z $(docker ps -q -a --filter ancestor=hertzsprung/thesis) ]]; then
  docker rm $(docker ps -q -a --filter ancestor=hertzsprung/thesis)
fi
if [[ ! -z $(docker volume ls -q --filter name=thesis-build) ]]; then
  docker volume rm thesis-build
fi

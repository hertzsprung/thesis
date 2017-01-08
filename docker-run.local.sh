#/bin/bash
set -e
if [ "$#" -lt 1 ]; then
  echo "Usage: ./docker-run.local.sh <docker.config> [docker cmd]"
  exit 1
fi

source $1; shift

docker volume create --opt type=none --opt device=$BUILD_DIR --opt o=bind thesis-build
docker run -it -v /home/jshaw/thesis:/home/phd/src/thesis -v thesis-build:/home/phd/build hertzsprung/thesis $@

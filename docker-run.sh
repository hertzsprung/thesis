#/bin/bash
set -e
source docker.config

docker volume create --opt type=none --opt device=$BUILD_DIR --opt o=bind thesis-build
docker run -it -v thesis-build:/home/phd/build hertzsprung/thesis $@

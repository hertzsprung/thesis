#/bin/bash
set -e
docker run -it -v /home/jshaw/thesis:/home/phd/src/thesis -v thesis-build:/home/phd/build hertzsprung/thesis $@

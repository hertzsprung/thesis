#!/bin/bash
set -e

display_usage() {
	echo -e "Usage: build.ninja.sh <builddir>\n"
}

if [  $# -lt 1 ]
then
	display_usage
	exit 1
fi

cat << EOF > build.ninja
builddir = $1
include build.main.ninja
EOF

ninja

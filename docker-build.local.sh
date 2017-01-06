#!/bin/bash
set -e
docker build -t hertzsprung/thesis:latest . $@

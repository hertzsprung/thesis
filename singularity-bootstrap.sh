#!/bin/bash
set -e

sudo singularity create --size 2560 thesis.img
sudo singularity bootstrap thesis.img Singularity

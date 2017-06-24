#!/bin/bash
set -e

sudo singularity create --size 3072 thesis.img
sudo singularity bootstrap thesis.img Singularity

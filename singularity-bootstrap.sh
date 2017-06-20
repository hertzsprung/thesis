#!/bin/bash
sudo singularity create --size 2560 thesis.img
sudo singularity bootstrap thesis.img Singularity

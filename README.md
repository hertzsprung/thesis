# Numerical representation of mountains in atmospheric models

## Compiling the thesis with Singularity
Use [Singularity](http://singularity.lbl.gov) to compile the thesis.  On Ubuntu 16.10 and later, `sudo apt-get install singularity-container`.  Once installed,

1. `./singularity.bootstrap.sh` to bootstrap the Singularity image, `thesis.img`
2. `./singularity.ninja.sh` to compile `thesis.pdf`

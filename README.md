# Numerical representation of mountains in atmospheric models

## Compiling the thesis with Singularity
Use [Singularity](http://singularity.lbl.gov) to compile the thesis.  On Ubuntu 16.10 and later, `sudo apt-get install singularity-container`.  

Once installed,

1. Execute the [AtmosTests](https://github.com/hertzsprung/AtmosTests) simulations
2. Edit `thesis/build.properties` so that `atmostests_builddir` points to the `AtmosTests/build` directory
3. Execute `./singularity.bootstrap.sh` to bootstrap the Singularity image, `thesis.img`
4. Execute `./singularity.ninja.sh` to compile `thesis.pdf`

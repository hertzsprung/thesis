from ninjaopenfoam import Gnuplot

import os

class Resting:
    def __init__(self):
        self.w = Gnuplot(
                'resting-w',
                output=os.path.join('thesis/slanted/resting/w'),
                plot=os.path.join('src/thesis/slanted/resting/w.plt'),
                data=[
                    '$atmostests_builddir/resting-btf-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-sleve-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-cutCell-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-slantedCell-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-btf-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-sleve-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-cutCell-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-slantedCell-cubicFit-collated/maxw.txt'
        ])

    def outputs(self):
        return self.w.outputs()

    def addTo(self, build):
        build.add(self.w)

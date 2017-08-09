from ninjaopenfoam import Gnuplot

import os

class Resting:
    def __init__(self):
        self.maxw = Gnuplot(
                'resting-maxw',
                output=os.path.join('thesis/slanted/resting/maxw'),
                plot=os.path.join('src/thesis/slanted/resting/maxw.plt'),
                data=[
                    '$atmostests_builddir/resting-btf-linearUpwind-collated/maxw.txt',
                    '$atmostests_builddir/resting-sleve-linearUpwind-collated/maxw.txt',
                    '$atmostests_builddir/resting-cutCell-linearUpwind-collated/maxw.txt',
                    '$atmostests_builddir/resting-slantedCell-linearUpwind-collated/maxw.txt',
                    '$atmostests_builddir/resting-btf-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-sleve-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-cutCell-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-slantedCell-cubicFit-collated/maxw.txt'
        ])

    def outputs(self):
        return self.maxw.outputs()

    def addTo(self, build):
        build.add(self.maxw)

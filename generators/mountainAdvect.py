from ninjaopenfoam import Gnuplot
import os

class MountainAdvect:
    def __init__(self):
        self.l2ByMountainHeight = Gnuplot(
                'mountainAdvect-l2ByMountainHeight',
                output=os.path.join('thesis/slanted/mountainAdvect/l2ByMountainHeight'),
                plot=os.path.join('src/thesis/slanted/mountainAdvect/l2ByMountainHeight.plt'),
                data=[
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-cubicFit-collated/10000/l2errorT.txt'
        ])

    def outputs(self):
        return self.l2ByMountainHeight.outputs()

    def addTo(self, build):
        build.add(self.l2ByMountainHeight)

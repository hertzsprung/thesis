from ninjaopenfoam import Gnuplot

import os

class SchaerAdvect:
    def __init__(self):
        self.convergence = Gnuplot(
                'cubicFit-schaerAdvect-convergence',
                output=os.path.join('thesis/cubicFit/schaerAdvect-convergence'),
                plot=os.path.join('src/thesis/cubicFit/schaerAdvect-convergence.plt'),
                data=[
                    '$atmostests_builddir/schaerAdvect-btf-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-linearUpwind-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-cubicFit-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-linearUpwind-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-cubicFit-collated/10000/linferrorT.txt'
        ])

    def outputs(self):
        return self.convergence.outputs()

    def addTo(self, build):
        build.add(self.convergence)

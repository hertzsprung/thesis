from ninjaopenfoam import Case, Gnuplot
import os

class SchaerAdvectSmooth:
    def __init__(self):
        self.convergence = Gnuplot(
                'highOrderFit-schaerAdvectSmooth-convergence',
                output=os.path.join('thesis/highOrderFit/schaerAdvectSmooth/convergence'),
                plot=os.path.join('src/thesis/highOrderFit/schaerAdvectSmooth/convergence.plt'),
                data=[
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-btf-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-btf-cubicFit-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-btf-highOrderFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-btf-highOrderFit-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-cutCell-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-cutCell-cubicFit-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-cutCell-highOrderFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvectSmooth-cos4-cutCell-highOrderFit-collated/10000/linferrorT.txt'
                ])

    def outputs(self):
        return self.convergence.outputs()

    def addTo(self, build):
        build.add(self.convergence)

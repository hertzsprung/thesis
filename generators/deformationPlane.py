from ninjaopenfoam import Case, Gnuplot
import os

class DeformationPlane:
    def __init__(self):
        self.convergence = Gnuplot(
                'highOrderFit-deformationPlane-convergence',
                output=os.path.join('thesis/highOrderFit/deformationPlane/convergence'),
                plot=os.path.join('src/thesis/highOrderFit/deformationPlane/convergence.plt'),
                data=[
                    '$atmostests_builddir/deformationPlane-uniform-cubicFit-collated/5/l2errorT.txt',
                    '$atmostests_builddir/deformationPlane-uniform-cubicFit-collated/5/linferrorT.txt',
                    '$atmostests_builddir/deformationPlane-uniform-highOrderFit-collated/5/l2errorT.txt',
                    '$atmostests_builddir/deformationPlane-uniform-highOrderFit-collated/5/linferrorT.txt'
                ])

    def outputs(self):
        return self.convergence.outputs()

    def addTo(self, build):
        build.add(self.convergence)

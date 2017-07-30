#!/usr/bin/python3

import generators
from ninjaopenfoam import Build, Case, Gnuplot, PDFLaTeX, Shortcuts
import os

class Thesis:
    def __init__(self):
        self.build = Build([
            'generators/deformationSphere.py',
            'generators/mountainAdvect.py'
        ])

    def write(self):
        build = self.build

        deformationSphere = generators.DeformationSphere()
        mountainAdvect = generators.MountainAdvect()

        stabilisation = Gnuplot(
                'cubicFit-stabilisation',
                output=os.path.join('thesis/cubicFit/stabilisation'),
                plot=os.path.join('src/thesis/cubicFit/stabilisation.plt'),
                data=[
                    os.path.join('src/thesis/cubicFit/centralQuad.dat'),
                    os.path.join('src/thesis/cubicFit/cubic.dat')
                ])

        schaerAdvectConvergence = Gnuplot(
                'cubicFit-schaerAdvect-convergence',
                output=os.path.join('thesis/cubicFit/schaerAdvect-convergence'),
                plot=os.path.join('src/thesis/cubicFit/schaerAdvect-convergence.plt'),
                data=[
                    '$atmostests_builddir/schaerAdvect-btf-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-linearUpwind-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-cubicFit-collated/10000/linferrorT.txt'
        ])

        thesis = PDFLaTeX(
                'thesis',
                output=os.path.join('thesis/thesis'),
                document=os.path.join('src/thesis/thesis'),
                components=[
                        'src/thesis/title.tex',
                        'src/thesis/mysouthall.tex',
                        'src/thesis/math.tex',
                        'src/thesis/thesis.bib',
                        'src/thesis/cubicFit.tex',
                        'src/thesis/cubicFit/transport.tex',
                        'src/thesis/cubicFit/scheme.tex',
                        'src/thesis/cubicFit/linearUpwind.tex',
                        'src/thesis/cubicFit/schaerAdvect.tex',
                        'src/thesis/cubicFit/deformationSphere.tex',
                        'src/thesis/cubicFit/interior-stencils.tex',
                        'src/thesis/cubicFit/double-upwind-stencil.tex',
                        'src/thesis/cubicFit/boundary-stencils.tex',
                        'src/thesis/cubicFit/vonNeumann.tex',
                        'src/thesis/cubicFit/spherical.tex',
                        'src/thesis/slanted.tex',
                        'src/thesis/slanted/mountainAdvect.tex',
                        'src/thesis/slanted/resting.tex']
                        + stabilisation.outputs()
                        + schaerAdvectConvergence.outputs()
                        + deformationSphere.outputs()
                        + mountainAdvect.outputs())

        shortcut = Shortcuts([thesis.output])

        build.add(stabilisation)
        build.add(schaerAdvectConvergence)
        deformationSphere.addTo(build)
        mountainAdvect.addTo(build)
        build.add(thesis)
        build.add(shortcut)

        build.write()


if __name__ == '__main__':
    Thesis().write()

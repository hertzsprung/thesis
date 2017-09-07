#!/usr/bin/python3

import generators
from ninjaopenfoam import Build, Case, Gnuplot, PDFLaTeX, Shortcuts
import os

class Thesis:
    def __init__(self):
        self.build = Build([
            'generators/deformationSphere.py',
            'generators/mountainAdvect.py',
            'generators/resting.py',
            'generators/schaerAdvect.py',
            'generators/schaerWaves.py',
            'generators/tfAdvect.py'
        ])

    def write(self):
        build = self.build

        schaerAdvect = generators.SchaerAdvect()
        deformationSphere = generators.DeformationSphere()
        mountainAdvect = generators.MountainAdvect()
        resting = generators.Resting()
        schaerWaves = generators.SchaerWaves()

        stabilisation = Gnuplot(
                'cubicFit-stabilisation',
                output=os.path.join('thesis/cubicFit/stabilisation'),
                plot=os.path.join('src/thesis/cubicFit/stabilisation.plt'),
                data=[
                    os.path.join('src/thesis/cubicFit/centralQuad.dat'),
                    os.path.join('src/thesis/cubicFit/cubic.dat')
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
                        'src/thesis/cubicFit/tfAdvect.tex',
                        'src/thesis/cubicFit/deformationSphere.tex',
                        'src/thesis/cubicFit/interior-stencils.tex',
                        'src/thesis/cubicFit/double-upwind-stencil.tex',
                        'src/thesis/cubicFit/boundary-stencils.tex',
                        'src/thesis/cubicFit/spherical.tex',
                        'src/thesis/slanted.tex',
                        'src/thesis/slanted/mountainAdvect.tex',
                        'src/thesis/slanted/resting.tex',
                        'src/thesis/slanted/schaerWaves.tex']
                        + stabilisation.outputs()
                        + schaerAdvect.outputs()
                        + deformationSphere.outputs()
                        + mountainAdvect.outputs()
                        + resting.outputs()
                        + schaerWaves.outputs())

        shortcuts = Shortcuts([thesis.output])

        build.add(stabilisation)
        schaerAdvect.addTo(build)
        deformationSphere.addTo(build)
        mountainAdvect.addTo(build)
        resting.addTo(build)
        schaerWaves.addTo(build)
        build.add(thesis)
        build.add(shortcuts)

        build.write()


if __name__ == '__main__':
    Thesis().write()

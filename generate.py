#!/usr/bin/python3

from ninjaopenfoam import Build, Case, Gnuplot, GmtPlot, PDFLaTeX, Shortcuts
import os

class DeformationSphere:
    gaussiansConvergence = Gnuplot(
            'deformationSphere-gaussiansConvergence',
            output=os.path.join('thesis/cubicFit/deformationSphere-gaussiansConvergence'),
            plot=os.path.join('src/thesis/cubicFit/deformationSphere-gaussiansConvergence.plt'))

    gaussiansInitialTracer = GmtPlot(
            'deformationSphere-gaussiansInitialTracer',
            plot=os.path.join('src/thesis/cubicFit/deformationSphere/tracer.gmtdict'),
            case=Case('deformationSphere-gaussians-hex-8-cubicFit', prefix='$atmostests_builddir'),
            time=0,
            data=['0/T'])

class Thesis:
    def __init__(self):
        self.build = Build()

    def write(self):
        build = self.build

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
                        'src/thesis/cubicFit/deformationSphere.tex',
                        'src/thesis/cubicFit/interior-stencils.tex',
                        'src/thesis/cubicFit/double-upwind-stencil.tex',
                        'src/thesis/cubicFit/boundary-stencils.tex'] +
                        stabilisation.outputs() +
                        DeformationSphere.gaussiansConvergence.outputs() +
                        DeformationSphere.gaussiansInitialTracer.outputs())

        shortcut = Shortcuts([thesis.output])

        build.add(stabilisation)
        build.add(DeformationSphere.gaussiansConvergence)
        build.add(DeformationSphere.gaussiansInitialTracer)
        build.add(thesis)
        build.add(shortcut)

        build.write()


if __name__ == '__main__':
    Thesis().write()

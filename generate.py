#!/usr/bin/python3

from ninjaopenfoam import Build, Case, Gnuplot, GmtPlot, GmtPlotCopyCase, PDFLaTeX, Shortcuts
import os

class DeformationSphere:
    def __init__(self):
        self.gaussiansConvergence = Gnuplot(
                'deformationSphere-gaussiansConvergence',
                output=os.path.join('thesis/cubicFit/deformationSphere-gaussiansConvergence'),
                plot=os.path.join('src/thesis/cubicFit/deformationSphere-gaussiansConvergence.plt'),
                data=[
                    '$atmostests_builddir/deformationSphere-gaussians-hex-linearUpwind-collated/1036800/l2errorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-hex-cubicFit-collated/1036800/l2errorT.txt',
#                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-linearUpwind-collated/1036800/l2errorT.txt',
#                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-cubicFit-collated/1036800/l2errorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-hex-linearUpwind-collated/1036800/linferrorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-hex-cubicFit-collated/1036800/linferrorT.txt',
#                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-linearUpwind-collated/1036800/linferrorT.txt',
#                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-cubicFit-collated/1036800/linferrorT.txt'
        ])

        self.gaussiansHex8cubicFit = GmtPlotCopyCase(
                'deformationSphere-gaussians-hex-8-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=[
                    'src/thesis/cubicFit/deformationSphere/tracer.gmtdict',
                    'src/thesis/cubicFit/deformationSphere/tracerW.gmtdict',
                ],
                files=[
                    '0/T',
                    '518400/T',
                    '1036800/T'
                ])

        gaussiansHex8cubicFitCase = Case('deformationSphere-gaussians-hex-8-cubicFit')

        self.gaussiansInitialTracer = GmtPlot(
            'deformationSphere-gaussiansInitialTracer',
            plot='tracer',
            case=gaussiansHex8cubicFitCase,
            time=0,
            data=['0/T'])

        self.gaussiansMidTracer = GmtPlot(
            'deformationSphere-gaussiansMidTracer',
            plot='tracerW',
            case=gaussiansHex8cubicFitCase,
            time=518400,
            data=['518400/T'])

        self.gaussiansFinalTracer = GmtPlot(
            'deformationSphere-gaussiansFinalTracer',
            plot='tracerW',
            case=gaussiansHex8cubicFitCase,
            time=1036800,
            data=['1036800/T'])

class Thesis:
    def __init__(self):
        self.build = Build()

    def write(self):
        build = self.build

        deformationSphere = DeformationSphere()

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
                        'src/thesis/cubicFit/boundary-stencils.tex']
                        + stabilisation.outputs()
                        + deformationSphere.gaussiansConvergence.outputs()
                        + deformationSphere.gaussiansInitialTracer.outputs()
                        + deformationSphere.gaussiansMidTracer.outputs()
                        + deformationSphere.gaussiansFinalTracer.outputs())

        shortcut = Shortcuts([thesis.output])

        build.add(stabilisation)
        build.add(deformationSphere.gaussiansHex8cubicFit)
        build.add(deformationSphere.gaussiansConvergence)
        build.add(deformationSphere.gaussiansInitialTracer)
        build.add(deformationSphere.gaussiansMidTracer)
        build.add(deformationSphere.gaussiansFinalTracer)
        build.add(thesis)
        build.add(shortcut)

        build.write()


if __name__ == '__main__':
    Thesis().write()

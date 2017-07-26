#!/usr/bin/python3

from ninjaopenfoam import Build, Case, Gnuplot, GmtPlot, GmtPlotCopyCase, PDFLaTeX, Shortcuts, siunitx
import os

class DeformationSphere:
    def __init__(self):
        self.gaussiansConvergence = Gnuplot(
                'deformationSphere-gaussiansConvergence',
                output=os.path.join('thesis/cubicFit/deformationSphere/gaussiansConvergence'),
                plot=os.path.join('src/thesis/cubicFit/deformationSphere/gaussiansConvergence.plt'),
                data=[
                    '$atmostests_builddir/deformationSphere-gaussians-hex-linearUpwind-collated/1036800/l2errorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-hex-cubicFit-collated/1036800/l2errorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-linearUpwind-collated/1036800/l2errorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-cubicFit-collated/1036800/l2errorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-hex-linearUpwind-collated/1036800/linferrorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-hex-cubicFit-collated/1036800/linferrorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-linearUpwind-collated/1036800/linferrorT.txt',
                    '$atmostests_builddir/deformationSphere-gaussians-cubedSphere-cubicFit-collated/1036800/linferrorT.txt'
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
            data=['0/T'],
            colorBar='legends/tracer_T.eps')

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

        self.coarsestSpacing = siunitx.Ang(
                '$atmostests_builddir/deformationSphere-mesh-hex-4',
                'averageEquatorialSpacing.txt')

        self.hex8Spacing = siunitx.Ang(
                '$atmostests_builddir/deformationSphere-mesh-hex-8',
                'averageEquatorialSpacing.txt')

        self.finestSpacing = siunitx.Ang(
                '$atmostests_builddir/deformationSphere-mesh-hex-9',
                'averageEquatorialSpacing.txt')

    def outputs(self):
        return self.gaussiansConvergence.outputs() \
            + self.gaussiansInitialTracer.outputs() \
            + self.gaussiansMidTracer.outputs() \
            + self.gaussiansFinalTracer.outputs() \
            + self.coarsestSpacing.outputs() \
            + self.finestSpacing.outputs() \
            + self.hex8Spacing.outputs()

    def addTo(self, build):
        build.add(self.gaussiansHex8cubicFit)
        build.add(self.gaussiansConvergence)
        build.add(self.gaussiansInitialTracer)
        build.add(self.gaussiansMidTracer)
        build.add(self.gaussiansFinalTracer)
        build.add(self.coarsestSpacing)
        build.add(self.finestSpacing)
        build.add(self.hex8Spacing)

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
                        + deformationSphere.outputs())

        shortcut = Shortcuts([thesis.output])

        build.add(stabilisation)
        build.add(schaerAdvectConvergence)
        deformationSphere.addTo(build)
        build.add(thesis)
        build.add(shortcut)

        build.write()


if __name__ == '__main__':
    Thesis().write()

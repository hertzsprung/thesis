from ninjaopenfoam import Case, Gnuplot, GmtPlot, GmtPlotCopyCase, siunitx

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

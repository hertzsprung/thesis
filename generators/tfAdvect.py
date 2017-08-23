from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase, Gnuplot, Paths, PDFLaTeXFigure, siunitx
import itertools
import os

class TfAdvect:
    def __init__(self):
        self.copyCases()
        self.heatmaps()

        self.btfTimestep = siunitx.Timestep(
                'tfAdvect-btf-1000-dt', '$atmostests_builddir/tfAdvect-btf-1000-linearUpwind')

        self.cutCellTimestep = siunitx.Timestep(
                'tfAdvect-cutCell-1000-dt', '$atmostests_builddir/tfAdvect-cutCell-1000-linearUpwind')

        self.tracerPlot = GmtPlot(
            'tfAdvect-btfCubicFitTracer',
            plot='tracer',
            case=Case('tfAdvect-btf-1000-cubicFit'),
            time=10000,
            data=[
                '10000/T_0',
                '10000/T_5000',
                '10000/T',
                '10000/T_analytic'
            ]
        )

        self.tracerFigure = PDFLaTeXFigure(
                'tfAdvect-fig-tracer',
                output=os.path.join('thesis/cubicFit/tfAdvect/fig-tracer'),
                figure=os.path.join('src/thesis/cubicFit/tfAdvect/fig-tracer'),
                components=self.tracerPlot.outputs()
        )

    def copyCases(self):
        self.btfLinearUpwind = GmtPlotCopyCase(
                'tfAdvect-btf-1000-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cubicFit/schaerAdvect/errorW.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCellLinearUpwind = GmtPlotCopyCase(
                'tfAdvect-cutCell-1000-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cubicFit/schaerAdvect/error.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.btfCubicFit = GmtPlotCopyCase(
                'tfAdvect-btf-1000-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=[
                    'src/thesis/cubicFit/schaerAdvect/errorSW.gmtdict',
                    'src/thesis/cubicFit/tfAdvect/tracer.gmtdict'
                ],
                files=['10000/T', '10000/T_analytic', '10000/T_diff'],
                renamedFiles={'0/T': '10000/T_0', '5000/T': '10000/T_5000'}
        )

        self.cutCellCubicFit = GmtPlotCopyCase(
                'tfAdvect-cutCell-1000-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cubicFit/schaerAdvect/errorS.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

    def heatmaps(self):
        self.btfLinearUpwindError = GmtPlot(
            'tfAdvect-btfLinearUpwindError',
            plot='errorW',
            case=Case('tfAdvect-btf-1000-linearUpwind'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCellLinearUpwindError = GmtPlot(
            'tfAdvect-cutCellLinearUpwindError',
            plot='error',
            case=Case('tfAdvect-cutCell-1000-linearUpwind'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.btfCubicFitError = GmtPlot(
            'tfAdvect-btfCubicFitError',
            plot='errorSW',
            case=Case('tfAdvect-btf-1000-cubicFit'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCellCubicFitError = GmtPlot(
            'tfAdvect-cutCellCubicFitError',
            plot='errorS',
            case=Case('tfAdvect-cutCell-1000-cubicFit'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.heatmapL2Errors = [
            siunitx.Num('tfAdvect-btf-1000-linearUpwind-l2error', '$atmostests_builddir/tfAdvect-btf-1000-linearUpwind', '10000/l2errorT.txt'),
            siunitx.Num('tfAdvect-cutCell-1000-linearUpwind-l2error', '$atmostests_builddir/tfAdvect-cutCell-1000-linearUpwind', '10000/l2errorT.txt'),
            siunitx.Num('tfAdvect-btf-1000-cubicFit-l2error', '$atmostests_builddir/tfAdvect-btf-1000-cubicFit', '10000/l2errorT.txt'),
            siunitx.Num('tfAdvect-cutCell-1000-cubicFit-l2error', '$atmostests_builddir/tfAdvect-cutCell-1000-cubicFit', '10000/l2errorT.txt')
        ]

        self.heatmapLinfErrors = [
            siunitx.Num('tfAdvect-btf-1000-linearUpwind-linferror', '$atmostests_builddir/tfAdvect-btf-1000-linearUpwind', '10000/linferrorT.txt'),
            siunitx.Num('tfAdvect-cutCell-1000-linearUpwind-linferror', '$atmostests_builddir/tfAdvect-cutCell-1000-linearUpwind', '10000/linferrorT.txt'),
            siunitx.Num('tfAdvect-btf-1000-cubicFit-linferror', '$atmostests_builddir/tfAdvect-btf-1000-cubicFit', '10000/linferrorT.txt'),
            siunitx.Num('tfAdvect-cutCell-1000-cubicFit-linferror', '$atmostests_builddir/tfAdvect-cutCell-1000-cubicFit', '10000/linferrorT.txt')
        ]

    def outputs(self):
        return self.btfLinearUpwindError.outputs() \
             + self.cutCellLinearUpwindError.outputs() \
             + self.btfCubicFitError.outputs() \
             + self.cutCellCubicFitError.outputs() \
             + list(itertools.chain.from_iterable([e.outputs() for e in self.heatmapL2Errors])) \
             + list(itertools.chain.from_iterable([e.outputs() for e in self.heatmapLinfErrors])) \
             + self.tracerFigure.outputs() \
             + self.btfTimestep.outputs() \
             + self.cutCellTimestep.outputs()

    def addTo(self, build):
        build.add(self.btfLinearUpwind)
        build.add(self.cutCellLinearUpwind)
        build.add(self.btfCubicFit)
        build.add(self.cutCellCubicFit)

        build.add(self.btfLinearUpwindError)
        build.add(self.cutCellLinearUpwindError)
        build.add(self.btfCubicFitError)
        build.add(self.cutCellCubicFitError)
        build.addAll(self.heatmapL2Errors)
        build.addAll(self.heatmapLinfErrors)

        build.add(self.btfTimestep)
        build.add(self.cutCellTimestep)

        build.add(self.tracerPlot)
        build.add(self.tracerFigure)

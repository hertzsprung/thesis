from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase, Gnuplot, siunitx
import itertools
import os

class SchaerAdvect:
    def __init__(self):
        self.copyCases()
        self.heatmaps()

        self.convergence = Gnuplot(
                'cubicFit-schaerAdvect-convergence',
                output=os.path.join('thesis/cubicFit/schaerAdvect/convergence'),
                plot=os.path.join('src/thesis/cubicFit/schaerAdvect/convergence.plt'),
                data=[
                    '$atmostests_builddir/schaerAdvect-btf-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-linearUpwind-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvect-btf-cubicFit-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-linearUpwind-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/schaerAdvect-cutCell-cubicFit-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/tfAdvect-btf-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/tfAdvect-btf-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/tfAdvect-btf-linearUpwind-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/tfAdvect-btf-cubicFit-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/tfAdvect-cutCell-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/tfAdvect-cutCell-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/tfAdvect-cutCell-linearUpwind-collated/10000/linferrorT.txt',
                    '$atmostests_builddir/tfAdvect-cutCell-cubicFit-collated/10000/linferrorT.txt'
        ])

    def copyCases(self):
        self.btfLinearUpwind = GmtPlotCopyCase(
                'schaerAdvect-btf-1000-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cubicFit/schaerAdvect/errorW.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCellLinearUpwind = GmtPlotCopyCase(
                'schaerAdvect-cutCell-1000-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cubicFit/schaerAdvect/error.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.btfCubicFit = GmtPlotCopyCase(
                'schaerAdvect-btf-1000-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cubicFit/schaerAdvect/errorSW.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCellCubicFit = GmtPlotCopyCase(
                'schaerAdvect-cutCell-1000-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cubicFit/schaerAdvect/errorS.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

    def heatmaps(self):
        self.btfLinearUpwindError = GmtPlot(
            'schaerAdvect-btfLinearUpwindError',
            plot='errorW',
            case=Case('schaerAdvect-btf-1000-linearUpwind'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCellLinearUpwindError = GmtPlot(
            'schaerAdvect-cutCellLinearUpwindError',
            plot='error',
            case=Case('schaerAdvect-cutCell-1000-linearUpwind'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.btfCubicFitError = GmtPlot(
            'schaerAdvect-btfCubicFitError',
            plot='errorSW',
            case=Case('schaerAdvect-btf-1000-cubicFit'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCellCubicFitError = GmtPlot(
            'schaerAdvect-cutCellCubicFitError',
            plot='errorS',
            case=Case('schaerAdvect-cutCell-1000-cubicFit'),
            time=10000,
            data=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.heatmapL2Errors = [
            siunitx.Num('schaerAdvect-btf-1000-linearUpwind-l2error', '$atmostests_builddir/schaerAdvect-btf-1000-linearUpwind', '10000/l2errorT.txt'),
            siunitx.Num('schaerAdvect-cutCell-1000-linearUpwind-l2error', '$atmostests_builddir/schaerAdvect-cutCell-1000-linearUpwind', '10000/l2errorT.txt'),
            siunitx.Num('schaerAdvect-btf-1000-cubicFit-l2error', '$atmostests_builddir/schaerAdvect-btf-1000-cubicFit', '10000/l2errorT.txt'),
            siunitx.Num('schaerAdvect-cutCell-1000-cubicFit-l2error', '$atmostests_builddir/schaerAdvect-cutCell-1000-cubicFit', '10000/l2errorT.txt')
        ]

        self.heatmapLinfErrors = [
            siunitx.Num('schaerAdvect-btf-1000-linearUpwind-linferror', '$atmostests_builddir/schaerAdvect-btf-1000-linearUpwind', '10000/linferrorT.txt'),
            siunitx.Num('schaerAdvect-cutCell-1000-linearUpwind-linferror', '$atmostests_builddir/schaerAdvect-cutCell-1000-linearUpwind', '10000/linferrorT.txt'),
            siunitx.Num('schaerAdvect-btf-1000-cubicFit-linferror', '$atmostests_builddir/schaerAdvect-btf-1000-cubicFit', '10000/linferrorT.txt'),
            siunitx.Num('schaerAdvect-cutCell-1000-cubicFit-linferror', '$atmostests_builddir/schaerAdvect-cutCell-1000-cubicFit', '10000/linferrorT.txt')
        ]

    def outputs(self):
        return self.convergence.outputs() \
             + self.btfLinearUpwindError.outputs() \
             + self.cutCellLinearUpwindError.outputs() \
             + self.btfCubicFitError.outputs() \
             + self.cutCellCubicFitError.outputs() \
             + list(itertools.chain.from_iterable([e.outputs() for e in self.heatmapL2Errors])) \
             + list(itertools.chain.from_iterable([e.outputs() for e in self.heatmapLinfErrors]))

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

        build.add(self.convergence)

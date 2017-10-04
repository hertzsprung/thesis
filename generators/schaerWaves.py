from ninjaopenfoam import Case, Gnuplot, GmtPlot, GmtPlotCopyCase, PDFLaTeXFigure

import os

class SchaerWaves:
    def __init__(self):
        self.linearUpwindW()
        self.thetaDiff()
        self.sampleLines()

    def linearUpwindW(self):
        self.btf300dzLinearUpwind = GmtPlotCopyCase(
                'schaerWaves-btf-300dz-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/schaerWaves/w.gmtdict'],
                files=['18000/Uf'])

        btf300dzLinearUpwindCase = Case('schaerWaves-btf-300dz-linearUpwind')

        self.btf300dzLinearUpwindW = GmtPlot(
            'schaerWaves-btf-300dz-linearUpwind-w',
            plot='w',
            case=btf300dzLinearUpwindCase,
            time=18000,
            data=['18000/Uf'])

        self.btf300dzLinearUpwindWFigure = PDFLaTeXFigure(
                'schaerWaves-btf-300dz-linearUpwind-w-figure',
                output=os.path.join('thesis/slanted/schaerWaves/fig-btf-300dz-linearUpwind-w'),
                figure=os.path.join('src/thesis/slanted/schaerWaves/fig-btf-300dz-linearUpwind-w'),
                components=self.btf300dzLinearUpwindW.outputs()
        )

    def thetaDiff(self):
        self.btf50dzCubicFit = GmtPlotCopyCase(
                'schaerWaves-btf-50dz-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/schaerWaves/thetaDiff.gmtdict'],
                files=['18000/theta_diff'])

        btf50dzCubicFitCase = Case('schaerWaves-btf-50dz-cubicFit')

        self.btf50dzCubicFitThetaDiff = GmtPlot(
            'schaerWaves-btf-50dz-cubicFit-thetaDiff',
            plot='thetaDiff',
            case=btf50dzCubicFitCase,
            time=18000,
            data=['18000/theta_diff'],
            colorBar='legends/thetaDiff_theta_diff.eps')

        self.btf50dzCubicFitThetaDiffFigure = PDFLaTeXFigure(
                'schaerWaves-btf-50dz-cubicFit-thetaDiff-figure',
                output=os.path.join('thesis/slanted/schaerWaves/fig-btf-50dz-cubicFit-thetaDiff'),
                figure=os.path.join('src/thesis/slanted/schaerWaves/fig-btf-50dz-cubicFit-thetaDiff'),
                components=self.btf50dzCubicFitThetaDiff.outputs()
        )

    def sampleLines(self):
        self.sampleLines = Gnuplot(
            'schaerWaves-sampleLines',
            output=os.path.join('thesis/slanted/schaerWaves/sampleLines'),
            plot=os.path.join('src/thesis/slanted/schaerWaves/sampleLines.plt'),
            data=[
                '$atmostests_builddir/schaerWaves-btf-500dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-300dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-250dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-200dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-150dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-125dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-100dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-75dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-btf-50dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-500dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-300dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-250dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-200dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-150dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-125dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-100dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-75dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-cutCell-50dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-500dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-300dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-250dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-200dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-150dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-125dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-100dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-75dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/schaerWaves-slantedCell-50dz-cubicFit/18000/theta_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-500dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-300dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-250dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-200dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-150dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-125dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-100dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-75dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-btf-50dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-500dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-300dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-250dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-200dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-150dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-125dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-100dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-75dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-cutCell-50dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-500dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-300dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-250dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-200dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-150dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-125dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-100dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-75dz-cubicFit/18000/T_diff.sampleLine.dat',
                '$atmostests_builddir/thermalAdvect-slantedCell-50dz-cubicFit/18000/T_diff.sampleLine.dat',
        ])

    def outputs(self):
        return ['src/thesis/slanted/schaerWaves/melvin2010-w-mass-conserving-sisl.png'] \
             + self.btf300dzLinearUpwindWFigure.outputs() \
             + self.btf50dzCubicFitThetaDiffFigure.outputs() \
             + self.sampleLines.outputs()

    def addTo(self, build):
        build.add(self.btf300dzLinearUpwind)
        build.add(self.btf50dzCubicFit)

        build.add(self.btf300dzLinearUpwindW)
        build.add(self.btf300dzLinearUpwindWFigure)

        build.add(self.btf50dzCubicFitThetaDiff)
        build.add(self.btf50dzCubicFitThetaDiffFigure)

        build.add(self.sampleLines)

from ninjaopenfoam import Case, Gnuplot, GmtPlot, GmtPlotCopyCase, PDFLaTeXFigure

import os

class SchaerWaves:
    def __init__(self):
        self.linearUpwindW()
        self.cubicFitW()
        self.charneyPhillipsW()

    def linearUpwindW(self):
        self.btf300dzLinearUpwind = GmtPlotCopyCase(
                'schaerWaves-btf-300dz-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cp/schaerWaves/w.gmtdict'],
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
                output=os.path.join('thesis/cp/schaerWaves/fig-btf-300dz-linearUpwind-w'),
                figure=os.path.join('src/thesis/cp/schaerWaves/fig-btf-300dz-linearUpwind-w'),
                components=self.btf300dzLinearUpwindW.outputs()
        )

    def cubicFitW(self):
        self.btf300dzCubicFit = GmtPlotCopyCase(
                'schaerWaves-btf-300dz-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cp/schaerWaves/wS.gmtdict'],
                files=['18000/Uf'])

        btf300dzCubicFitCase = Case('schaerWaves-btf-300dz-cubicFit')

        self.btf300dzCubicFitW = GmtPlot(
            'schaerWaves-btf-300dz-cubicFit-w',
            plot='wS',
            case=btf300dzCubicFitCase,
            time=18000,
            data=['18000/Uf'])

        self.btf300dzCubicFitWFigure = PDFLaTeXFigure(
                'schaerWaves-btf-300dz-cubicFit-w-figure',
                output=os.path.join('thesis/cp/schaerWaves/fig-btf-300dz-cubicFit-w'),
                figure=os.path.join('src/thesis/cp/schaerWaves/fig-btf-300dz-cubicFit-w'),
                components=self.btf300dzCubicFitW.outputs()
        )

    def charneyPhillipsW(self):
        self.btf300dzCharneyPhillips = GmtPlotCopyCase(
                'schaerWavesCP-btf-300dz',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cp/schaerWaves/w.gmtdict'],
                files=['18000/Uf'])

        btf300dzCharneyPhillipsCase = Case('schaerWavesCP-btf-300dz')

        self.btf300dzCharneyPhillipsW = GmtPlot(
            'schaerWavesCP-btf-300dz-w',
            plot='w',
            case=btf300dzCharneyPhillipsCase,
            time=18000,
            data=['18000/Uf'])

        self.btf300dzCharneyPhillipsWFigure = PDFLaTeXFigure(
                'schaerWaves-btf-300dz-cp-w-figure',
                output=os.path.join('thesis/cp/schaerWaves/fig-btf-300dz-cp-w'),
                figure=os.path.join('src/thesis/cp/schaerWaves/fig-btf-300dz-cp-w'),
                components=self.btf300dzCharneyPhillipsW.outputs()
        )

    def outputs(self):
        return ['src/thesis/cp/schaerWaves/melvin2010-w-mass-conserving-sisl.png'] \
             + self.btf300dzLinearUpwindWFigure.outputs() \
             + self.btf300dzCubicFitWFigure.outputs() \
             + self.btf300dzCharneyPhillipsWFigure.outputs()

    def addTo(self, build):
        build.add(self.btf300dzLinearUpwind)
        build.add(self.btf300dzCubicFit)
        build.add(self.btf300dzCharneyPhillips)

        build.add(self.btf300dzLinearUpwindW)
        build.add(self.btf300dzLinearUpwindWFigure)
        build.add(self.btf300dzCubicFitW)
        build.add(self.btf300dzCubicFitWFigure)
        build.add(self.btf300dzCharneyPhillipsW)
        build.add(self.btf300dzCharneyPhillipsWFigure)

from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase, PDFLaTeXFigure

import os

class SchaerWaves:
    def __init__(self):
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
                figure=os.path.join('src/thesis/slanted/mountainAdvect/fig-btf-300dz-linearUpwind-w'),
                components=self.btf300dzLinearUpwindW.outputs()
        )

    def outputs(self):
        return ['src/thesis/slanted/schaerWaves/melvin2010-w-mass-conserving-sisl.png'] \
             + self.btf300dzLinearUpwindWFigure.outputs()

    def addTo(self, build):
        build.add(self.btf300dzLinearUpwind)
        build.add(self.btf300dzLinearUpwindW)
        build.add(self.btf300dzLinearUpwindWFigure)

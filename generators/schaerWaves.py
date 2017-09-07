from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase

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

    def outputs(self):
        return ['src/thesis/slanted/schaerWaves/melvin2010-w-mass-conserving-sisl.png'] \
             + self.btf300dzLinearUpwindW.outputs()

    def addTo(self, build):
        build.add(self.btf300dzLinearUpwind)
        build.add(self.btf300dzLinearUpwindW)

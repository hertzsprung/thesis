from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase, PDFLaTeXFigure

import os

class ThermalAdvect:
    def __init__(self):
        self.btf = GmtPlotCopyCase(
                'thermalAdvect-btf-50dz-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/thermalAdvect/error.gmtdict'],
                files=['18000/T_diff', '18000/T']
        )

        self.cutCell = GmtPlotCopyCase(
                'thermalAdvect-cutCell-50dz-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/thermalAdvect/errorS.gmtdict'],
                files=['18000/T_diff', '18000/T']
        )

        self.btfError = GmtPlot(
                'thermalAdvect-btfError',
                plot='error',
                case=Case('thermalAdvect-btf-50dz-cubicFit'),
                time=18000,
                data=['18000/T_diff', '18000/T'],
                colorBar='legends/error_T_diff.eps'
        )

        self.cutCellError = GmtPlot(
                'thermalAdvect-cutCellError',
                plot='errorS',
                case=Case('thermalAdvect-cutCell-50dz-cubicFit'),
                time=18000,
                data=['18000/T_diff', '18000/T']
        )

        self.errorFigure = PDFLaTeXFigure(
                'thermalAdvect-fig-error',
                output=os.path.join('thesis/slanted/thermalAdvect/fig-error'),
                figure=os.path.join('src/thesis/slanted/thermalAdvect/fig-error'),
                components=self.btfError.outputs() + self.cutCellError.outputs())

    def outputs(self):
        return self.errorFigure.outputs()

    def addTo(self, build):
        build.add(self.btf)
        build.add(self.cutCell)
        build.add(self.btfError)
        build.add(self.cutCellError)
        build.add(self.errorFigure)

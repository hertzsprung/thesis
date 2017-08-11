from ninjaopenfoam import Case, Gnuplot, GmtPlot, GmtPlotCopyCase, \
        LaTeXSubstitution, siunitx, Paths
import itertools
import os

class MountainAdvect:
    def __init__(self):
        self.copyCases()
        self.meshes()
        self.heatmaps()

        self.l2ByMountainHeight = Gnuplot(
                'mountainAdvect-l2ByMountainHeight',
                output=os.path.join('thesis/slanted/mountainAdvect/l2ByMountainHeight'),
                plot=os.path.join('src/thesis/slanted/mountainAdvect/l2ByMountainHeight.plt'),
                data=[
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-cubicFit-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-linearUpwind-collated/10000/l2errorT.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-cubicFit-collated/10000/l2errorT.txt'
        ])

        self.maxdt = Gnuplot(
                'mountainAdvect-maxdt',
                output=os.path.join('thesis/slanted/mountainAdvect/maxdt'),
                plot=os.path.join('src/thesis/slanted/mountainAdvect/maxdt.plt'),
                data=[
                    '$atmostests_builddir/mountainAdvect-maxdt-btf-6000m-cubicFit-collated/dt.txt',
                    '$atmostests_builddir/mountainAdvect-maxdt-btf-6000m-cubicFit-collated/co.txt',
                    '$atmostests_builddir/mountainAdvect-maxdt-cutCell-6000m-cubicFit-collated/dt.txt',
                    '$atmostests_builddir/mountainAdvect-maxdt-cutCell-6000m-cubicFit-collated/co.txt',
                    '$atmostests_builddir/mountainAdvect-maxdt-slantedCell-6000m-cubicFit-collated/dt.txt',
                    '$atmostests_builddir/mountainAdvect-maxdt-slantedCell-6000m-cubicFit-collated/co.txt'
        ])

        self.timesteps = LaTeXSubstitution(
                'mountainAdvect-timesteps',
                output=os.path.join('thesis/slanted/mountainAdvect/timesteps'),
                input=os.path.join('src/thesis/slanted/mountainAdvect/timesteps.template'),
                data=[
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-0m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-3000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-4000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-5000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-btf-1000-6000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-0m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-3000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-4000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-5000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-6000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-0m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-3000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-4000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind/dt.txt',
                    '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind/dt.txt'
        ])

        self.unstableCourantNumber = siunitx.Num(
                'mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind-co',
                '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind',
                Paths.courantNumber)

    def copyCases(self):
        self.btf5000mLinearUpwind = GmtPlotCopyCase(
                'mountainAdvect-h0-btf-1000-5000m-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=[
                    'src/thesis/slanted/mountainAdvect/meshW.gmtdict',
                    'src/thesis/slanted/mountainAdvect/errorW.gmtdict'
                ],
                files=[
                    '10000/T',
                    '10000/T_analytic',
                    '10000/T_diff'
                ]
        )

        self.cutCell5000mLinearUpwind = GmtPlotCopyCase(
                'mountainAdvect-h0-cutCell-1000-5000m-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=[
                    'src/thesis/slanted/mountainAdvect/meshW.gmtdict',
                    'src/thesis/slanted/mountainAdvect/error.gmtdict'
                ],
                files=[
                    '10000/T',
                    '10000/T_analytic',
                    '10000/T_diff'
                ]
        )

        self.slantedCell5000mLinearUpwind = GmtPlotCopyCase(
                'mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=[
                    'src/thesis/slanted/mountainAdvect/mesh.gmtdict',
                    'src/thesis/slanted/mountainAdvect/error.gmtdict'
                ],
                files=[
                    '10000/T',
                    '10000/T_analytic',
                    '10000/T_diff'
                ]
        )

        self.btf5000mCubicFit = GmtPlotCopyCase(
                'mountainAdvect-h0-btf-1000-5000m-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/mountainAdvect/errorSW.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.cutCell5000mCubicFit = GmtPlotCopyCase(
                'mountainAdvect-h0-cutCell-1000-5000m-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/mountainAdvect/errorS.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

        self.slantedCell5000mCubicFit = GmtPlotCopyCase(
                'mountainAdvect-h0-slantedCell-1000-5000m-cubicFit',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/mountainAdvect/errorS.gmtdict'],
                files=['10000/T', '10000/T_analytic', '10000/T_diff']
        )

    def meshes(self):
        self.btfMesh = GmtPlot(
            'mountainAdvect-btfMesh',
            plot='meshW',
            case=Case('mountainAdvect-h0-btf-1000-5000m-linearUpwind'),
            time='constant'
        )

        self.cutCellMesh = GmtPlot(
            'mountainAdvect-cutCellMesh',
            plot='meshW',
            case=Case('mountainAdvect-h0-cutCell-1000-5000m-linearUpwind'),
            time='constant'
        )

        self.slantedCellMesh = GmtPlot(
            'mountainAdvect-slantedCellMesh',
            plot='mesh',
            case=Case('mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind'),
            time='constant'
        )

    def heatmaps(self):
        self.btfLinearUpwindError = GmtPlot(
            'mountainAdvect-btfLinearUpwindError',
            plot='errorW',
            case=Case('mountainAdvect-h0-btf-1000-5000m-linearUpwind'),
            time=10000,
            data=[
                '10000/T',
                '10000/T_analytic',
                '10000/T_diff'
            ]
        )

        self.cutCellLinearUpwindError = GmtPlot(
            'mountainAdvect-cutCellLinearUpwindError',
            plot='error',
            case=Case('mountainAdvect-h0-cutCell-1000-5000m-linearUpwind'),
            time=10000,
            data=[
                '10000/T',
                '10000/T_analytic',
                '10000/T_diff'
            ],
            colorBar='legends/error_T_diff.eps'
        )

        self.slantedCellLinearUpwindError = GmtPlot(
            'mountainAdvect-slantedCellLinearUpwindError',
            plot='error',
            case=Case('mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind'),
            time=10000,
            data=[
                '10000/T',
                '10000/T_analytic',
                '10000/T_diff'
            ]
        )

        self.btfCubicFitError = GmtPlot(
            'mountainAdvect-btfCubicFitError',
            plot='errorSW',
            case=Case('mountainAdvect-h0-btf-1000-5000m-cubicFit'),
            time=10000,
            data=[
                '10000/T',
                '10000/T_analytic',
                '10000/T_diff'
            ]
        )

        self.cutCellCubicFitError = GmtPlot(
            'mountainAdvect-cutCellCubicFitError',
            plot='errorS',
            case=Case('mountainAdvect-h0-cutCell-1000-5000m-cubicFit'),
            time=10000,
            data=[
                '10000/T',
                '10000/T_analytic',
                '10000/T_diff'
            ]
        )

        self.slantedCellCubicFitError = GmtPlot(
            'mountainAdvect-slantedCellCubicFitError',
            plot='errorS',
            case=Case('mountainAdvect-h0-slantedCell-1000-5000m-cubicFit'),
            time=10000,
            data=[
                '10000/T',
                '10000/T_analytic',
                '10000/T_diff'
            ]
        )

        self.heatmapL2Errors = [
            siunitx.Num('mountainAdvect-h0-btf-1000-5000m-linearUpwind-l2error', '$atmostests_builddir/mountainAdvect-h0-btf-1000-5000m-linearUpwind', '10000/l2errorT.txt'),
            siunitx.Num('mountainAdvect-h0-cutCell-1000-5000m-linearUpwind-l2error', '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-5000m-linearUpwind', '10000/l2errorT.txt'),
            siunitx.Num('mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind-l2error', '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind', '10000/l2errorT.txt'),
            siunitx.Num('mountainAdvect-h0-btf-1000-5000m-cubicFit-l2error', '$atmostests_builddir/mountainAdvect-h0-btf-1000-5000m-cubicFit', '10000/l2errorT.txt'),
            siunitx.Num('mountainAdvect-h0-cutCell-1000-5000m-cubicFit-l2error', '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-5000m-cubicFit', '10000/l2errorT.txt'),
            siunitx.Num('mountainAdvect-h0-slantedCell-1000-5000m-cubicFit-l2error', '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-5000m-cubicFit', '10000/l2errorT.txt')
        ]

        self.heatmapLinfErrors = [
            siunitx.Num('mountainAdvect-h0-btf-1000-5000m-linearUpwind-linferror', '$atmostests_builddir/mountainAdvect-h0-btf-1000-5000m-linearUpwind', '10000/linferrorT.txt'),
            siunitx.Num('mountainAdvect-h0-cutCell-1000-5000m-linearUpwind-linferror', '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-5000m-linearUpwind', '10000/linferrorT.txt'),
            siunitx.Num('mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind-linferror', '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind', '10000/linferrorT.txt'),
            siunitx.Num('mountainAdvect-h0-btf-1000-5000m-cubicFit-linferror', '$atmostests_builddir/mountainAdvect-h0-btf-1000-5000m-cubicFit', '10000/linferrorT.txt'),
            siunitx.Num('mountainAdvect-h0-cutCell-1000-5000m-cubicFit-linferror', '$atmostests_builddir/mountainAdvect-h0-cutCell-1000-5000m-cubicFit', '10000/linferrorT.txt'),
            siunitx.Num('mountainAdvect-h0-slantedCell-1000-5000m-cubicFit-linferror', '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-5000m-cubicFit', '10000/linferrorT.txt')
        ]

    def outputs(self):
        return self.btfMesh.outputs() \
                + self.cutCellMesh.outputs() \
                + self.slantedCellMesh.outputs() \
                + self.btfLinearUpwindError.outputs() \
                + self.cutCellLinearUpwindError.outputs() \
                + self.slantedCellLinearUpwindError.outputs() \
                + self.btfCubicFitError.outputs() \
                + self.cutCellCubicFitError.outputs() \
                + self.slantedCellCubicFitError.outputs() \
                + list(itertools.chain.from_iterable([e.outputs() for e in self.heatmapL2Errors])) \
                + list(itertools.chain.from_iterable([e.outputs() for e in self.heatmapLinfErrors])) \
                + self.l2ByMountainHeight.outputs() \
                + self.maxdt.outputs() \
                + self.timesteps.outputs() \
                + self.unstableCourantNumber.outputs()

    def addTo(self, build):
        build.add(self.btf5000mLinearUpwind)
        build.add(self.cutCell5000mLinearUpwind)
        build.add(self.slantedCell5000mLinearUpwind)
        build.add(self.btf5000mCubicFit)
        build.add(self.cutCell5000mCubicFit)
        build.add(self.slantedCell5000mCubicFit)

        build.add(self.btfMesh)
        build.add(self.cutCellMesh)
        build.add(self.slantedCellMesh)

        build.add(self.btfLinearUpwindError)
        build.add(self.cutCellLinearUpwindError)
        build.add(self.slantedCellLinearUpwindError)
        build.add(self.btfCubicFitError)
        build.add(self.cutCellCubicFitError)
        build.add(self.slantedCellCubicFitError)
        build.addAll(self.heatmapL2Errors)
        build.addAll(self.heatmapLinfErrors)

        build.add(self.l2ByMountainHeight)
        build.add(self.maxdt)
        build.add(self.timesteps)
        build.add(self.unstableCourantNumber)

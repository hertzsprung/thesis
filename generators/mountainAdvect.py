from ninjaopenfoam import Case, Gnuplot, GmtPlot, GmtPlotCopyCase, \
        LaTeXSubstitution, siunitx, Paths
import itertools
import os

class MountainAdvect:
    def __init__(self):
        self.btf5000mLinearUpwind = GmtPlotCopyCase(
                'mountainAdvect-h0-btf-1000-5000m-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/mountainAdvect/meshW.gmtdict']
        )

        self.cutCell5000mLinearUpwind = GmtPlotCopyCase(
                'mountainAdvect-h0-cutCell-1000-5000m-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/mountainAdvect/meshW.gmtdict']
        )

        self.slantedCell5000mLinearUpwind = GmtPlotCopyCase(
                'mountainAdvect-h0-slantedCell-1000-5000m-linearUpwind',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/mountainAdvect/mesh.gmtdict']
        )

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
                '$atmostests_builddir/mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind',
                Paths.courantNumber)

    def outputs(self):
        return self.btfMesh.outputs() \
                + self.cutCellMesh.outputs() \
                + self.slantedCellMesh.outputs() \
                + self.l2ByMountainHeight.outputs() \
                + self.maxdt.outputs() \
                + self.timesteps.outputs() \
                + self.unstableCourantNumber.outputs()

    def addTo(self, build):
        build.add(self.btf5000mLinearUpwind)
        build.add(self.btfMesh)
        build.add(self.cutCell5000mLinearUpwind)
        build.add(self.cutCellMesh)
        build.add(self.slantedCell5000mLinearUpwind)
        build.add(self.slantedCellMesh)
        build.add(self.l2ByMountainHeight)
        build.add(self.maxdt)
        build.add(self.timesteps)
        build.add(self.unstableCourantNumber)

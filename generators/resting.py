from ninjaopenfoam import Case, Gnuplot, GmtPlot, GmtPlotCopyCase, PDFLaTeXFigure, siunitx

import os

class Resting:
    def __init__(self):
        self.copyCases()
        self.meshes()
        self.meshesFigure = PDFLaTeXFigure(
                'resting-fig-meshes',
                output=os.path.join('thesis/slanted/resting/fig-meshes'),
                figure=os.path.join('src/thesis/slanted/resting/fig-meshes'),
                components=self.btfMesh.outputs() + \
                           self.sleveMesh.outputs() + \
                           self.cutCellMesh.outputs() + \
                           self.slantedCellMesh.outputs()
        )

        self.w = Gnuplot(
                'resting-w',
                output=os.path.join('thesis/slanted/resting/w'),
                plot=os.path.join('src/thesis/slanted/resting/w.plt'),
                data=[
                    '$atmostests_builddir/resting-btf-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-sleve-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-cutCell-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-slantedCell-1000m-cubicFit/energy.dat',
                    '$atmostests_builddir/resting-btf-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-sleve-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-cutCell-cubicFit-collated/maxw.txt',
                    '$atmostests_builddir/resting-slantedCell-cubicFit-collated/maxw.txt'
        ])

        self.btf1000mMaxW = siunitx.Velocity(
                'resting-btf-1000m-cubicFit-maxw',
                '$atmostests_builddir/resting-btf-1000m-cubicFit',
                'maxw.txt')

    def copyCases(self):
        self.btfMesh6000mCase = GmtPlotCopyCase(
                'resting-mesh-btf-6000m',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/resting/meshW.gmtdict']
        )

        self.sleveMesh6000mCase = GmtPlotCopyCase(
                'resting-mesh-sleve-6000m',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/resting/mesh.gmtdict']
        )

        self.cutCellMesh6000mCase = GmtPlotCopyCase(
                'resting-mesh-cutCell-6000m',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/resting/meshSW.gmtdict']
        )

        self.slantedCellMesh6000mCase = GmtPlotCopyCase(
                'resting-mesh-slantedCell-6000m',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/slanted/resting/meshS.gmtdict']
        )

    def meshes(self):
        self.btfMesh = GmtPlot(
            'resting-btfMesh',
            plot='meshW',
            case=Case('resting-mesh-btf-6000m'),
            time='constant'
        )

        self.sleveMesh = GmtPlot(
            'resting-sleveMesh',
            plot='mesh',
            case=Case('resting-mesh-sleve-6000m'),
            time='constant'
        )

        self.cutCellMesh = GmtPlot(
            'resting-cutCellMesh',
            plot='meshSW',
            case=Case('resting-mesh-cutCell-6000m'),
            time='constant'
        )

        self.slantedCellMesh = GmtPlot(
            'resting-slantedCellMesh',
            plot='meshS',
            case=Case('resting-mesh-slantedCell-6000m'),
            time='constant'
        )

    def outputs(self):
        return  self.meshesFigure.outputs() + \
                self.w.outputs() + \
                self.btf1000mMaxW.outputs()

    def addTo(self, build):
        build.add(self.meshesFigure)
        build.add(self.btfMesh6000mCase)
        build.add(self.sleveMesh6000mCase)
        build.add(self.cutCellMesh6000mCase)
        build.add(self.slantedCellMesh6000mCase)
        build.add(self.btfMesh)
        build.add(self.sleveMesh)
        build.add(self.cutCellMesh)
        build.add(self.slantedCellMesh)
        build.add(self.w)
        build.add(self.btf1000mMaxW)

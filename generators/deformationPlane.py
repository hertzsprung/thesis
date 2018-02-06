from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase, Gnuplot, PDFLaTeXFigure
import os

class DeformationPlane:
    def __init__(self):
        self.distortedMeshCase = GmtPlotCopyCase(
                'deformationPlane-mesh-distorted-6',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/highOrderFit/deformationPlane/mesh.gmtdict'])

        self.distortedMesh = GmtPlot(
            'deformationPlane-distortedMesh',
            plot='mesh',
            case=Case('deformationPlane-mesh-distorted-6'),
            time='constant')

        self.meshesFigure = PDFLaTeXFigure(
                'deformationPlane-fig-meshes',
                output=os.path.join('thesis/highOrderFit/deformationPlane/fig-meshes'),
                figure=os.path.join('src/thesis/highOrderFit/deformationPlane/fig-meshes'),
                components=self.distortedMesh.outputs())

        self.convergence = Gnuplot(
                'highOrderFit-deformationPlane-convergence',
                output=os.path.join('thesis/highOrderFit/deformationPlane/convergence'),
                plot=os.path.join('src/thesis/highOrderFit/deformationPlane/convergence.plt'),
                data=[
                    '$atmostests_builddir/deformationPlane-uniform-cubicFit-collated/5/l2errorT.txt',
                    '$atmostests_builddir/deformationPlane-uniform-cubicFit-collated/5/linferrorT.txt',
                    '$atmostests_builddir/deformationPlane-uniform-highOrderFit-collated/5/l2errorT.txt',
                    '$atmostests_builddir/deformationPlane-uniform-highOrderFit-collated/5/linferrorT.txt',
                    '$atmostests_builddir/deformationPlane-distorted-cubicFit-collated/5/l2errorT.txt',
                    '$atmostests_builddir/deformationPlane-distorted-cubicFit-collated/5/linferrorT.txt',
                    '$atmostests_builddir/deformationPlane-distorted-highOrderFit-collated/5/l2errorT.txt',
                    '$atmostests_builddir/deformationPlane-distorted-highOrderFit-collated/5/linferrorT.txt'
                ])

    def outputs(self):
        return self.meshesFigure.outputs() + \
                self.convergence.outputs()

    def addTo(self, build):
        build.add(self.distortedMeshCase)
        build.add(self.distortedMesh)
        build.add(self.meshesFigure)
        build.add(self.convergence)

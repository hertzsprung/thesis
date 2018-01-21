from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase, Gnuplot, PDFLaTeXFigure

import os

class ArakawaKonor:
    def __init__(self):
        self.copyCases()

        uniformLorenzCase = Case('arakawaKonor-uniform-lorenz')
        uniformCPCase = Case('arakawaKonor-uniform-cp')
        horizontalGradingLorenzCase = Case('arakawaKonor-horizontalGrading-lorenz')
        horizontalGradingCPCase = Case('arakawaKonor-horizontalGrading-cp')

        self.uniformInitialThetaDiff = GmtPlot(
            'arakawaKonor-uniform-initial-theta_diff',
            plot='theta_diffW',
            case=uniformLorenzCase,
            time=0,
            data=['0/theta_diff'],
            colorBar='legends/theta_diff.eps')

        self.uniformLorenzThetaDiff = GmtPlot(
            'arakawaKonor-uniform-lorenz-theta_diff',
            plot='theta_diffSW',
            case=uniformLorenzCase,
            time=172800,
            data=['172800/theta_diff'])

        self.uniformCPThetaDiff = GmtPlot(
            'arakawaKonor-uniform-cp-theta_diff',
            plot='theta_diffSW',
            case=uniformCPCase,
            time=172800,
            data=['172800/theta_diff'])

        self.horizontalGradingInitialThetaDiff = GmtPlot(
            'arakawaKonor-horizontalGrading-initial-theta_diff',
            plot='theta_diff',
            case=horizontalGradingLorenzCase,
            time=0,
            data=['0/theta_diff'])

        self.horizontalGradingLorenzThetaDiff = GmtPlot(
            'arakawaKonor-horizontalGrading-lorenz-theta_diff',
            plot='theta_diffS',
            case=horizontalGradingLorenzCase,
            time=172800,
            data=['172800/theta_diff'])

        self.horizontalGradingCPThetaDiff = GmtPlot(
            'arakawaKonor-horizontalGrading-cp-theta_diff',
            plot='theta_diffS',
            case=horizontalGradingCPCase,
            time=172800,
            data=['172800/theta_diff'])
        
        self.thetaDiffFigure = PDFLaTeXFigure(
                'arakawaKonor-fig-theta_diff',
                output=os.path.join('thesis/cp/arakawaKonor/fig-theta_diff'),
                figure=os.path.join('src/thesis/cp/arakawaKonor/fig-theta_diff'),
                components=self.uniformInitialThetaDiff.outputs() + \
                           self.uniformLorenzThetaDiff.outputs() + \
                           self.uniformCPThetaDiff.outputs() + \
                           self.horizontalGradingInitialThetaDiff.outputs() + \
                           self.horizontalGradingLorenzThetaDiff.outputs() + \
                           self.horizontalGradingCPThetaDiff.outputs()
        )

        self.meshes()
        self.meshesFigure = PDFLaTeXFigure(
                'arakawaKonor-fig-meshes',
                output=os.path.join('thesis/cp/arakawaKonor/fig-meshes'),
                figure=os.path.join('src/thesis/cp/arakawaKonor/fig-meshes'),
                components=self.horizontalGradedMesh.outputs() + \
                           self.verticalGradedMesh.outputs()
        )

        self.conservation = Gnuplot(
                'arakawaKonor-conservation',
                output=os.path.join('thesis/cp/arakawaKonor/conservation'),
                plot=os.path.join('src/thesis/cp/arakawaKonor/conservation.plt'),
                data=[
                    '$atmostests_builddir/arakawaKonor-uniform-lorenz/energy.dat',
                    '$atmostests_builddir/arakawaKonor-uniform-cp/energy.dat',
                    '$atmostests_builddir/arakawaKonor-horizontalGrading-lorenz/energy.dat',
                    '$atmostests_builddir/arakawaKonor-horizontalGrading-cp/energy.dat',
                    '$atmostests_builddir/arakawaKonor-verticalGrading-lorenz/energy.dat',
                    '$atmostests_builddir/arakawaKonor-verticalGrading-cp/energy.dat'
        ])

    def copyCases(self):
        self.uniformLorenz = GmtPlotCopyCase(
                'arakawaKonor-uniform-lorenz',
                source='$atmostests_builddir',
                target='$builddir',
                plots=[
                    'src/thesis/cp/arakawaKonor/theta_diffW.gmtdict',
                    'src/thesis/cp/arakawaKonor/theta_diffSW.gmtdict'
                ],
                files=['0/theta_diff', '172800/theta_diff'])

        self.uniformCP = GmtPlotCopyCase(
                'arakawaKonor-uniform-cp',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cp/arakawaKonor/theta_diffSW.gmtdict'],
                files=['172800/theta_diff'])

        self.horizontalGradingLorenz = GmtPlotCopyCase(
                'arakawaKonor-horizontalGrading-lorenz',
                source='$atmostests_builddir',
                target='$builddir',
                plots=[
                    'src/thesis/cp/arakawaKonor/meshW.gmtdict',
                    'src/thesis/cp/arakawaKonor/theta_diff.gmtdict',
                    'src/thesis/cp/arakawaKonor/theta_diffS.gmtdict'
                ],
                files=['0/theta_diff', '172800/theta_diff'])

        self.horizontalGradingCP = GmtPlotCopyCase(
                'arakawaKonor-horizontalGrading-cp',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cp/arakawaKonor/theta_diffS.gmtdict'],
                files=['172800/theta_diff'])

        self.verticalGradingLorenz = GmtPlotCopyCase(
                'arakawaKonor-verticalGrading-lorenz',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cp/arakawaKonor/mesh.gmtdict'])

    def meshes(self):
        self.horizontalGradedMesh = GmtPlot(
            'arakawaKonor-horizontalGradedMesh',
            plot='meshW',
            case=Case('arakawaKonor-horizontalGrading-lorenz'),
            time='constant'
        )

        self.verticalGradedMesh = GmtPlot(
            'arakawaKonor-verticalGradedMesh',
            plot='mesh',
            case=Case('arakawaKonor-verticalGrading-lorenz'),
            time='constant'
        )

    def outputs(self):
        return self.thetaDiffFigure.outputs() + \
               self.meshesFigure.outputs() + \
               self.conservation.outputs()

    def addTo(self, build):
        build.add(self.uniformLorenz)
        build.add(self.uniformCP)
        build.add(self.horizontalGradingLorenz)
        build.add(self.horizontalGradingCP)
        build.add(self.verticalGradingLorenz)

        build.add(self.uniformInitialThetaDiff)
        build.add(self.uniformLorenzThetaDiff)
        build.add(self.uniformCPThetaDiff)
        build.add(self.horizontalGradingInitialThetaDiff)
        build.add(self.horizontalGradingLorenzThetaDiff)
        build.add(self.horizontalGradingCPThetaDiff)
        build.add(self.thetaDiffFigure)

        build.add(self.horizontalGradedMesh)
        build.add(self.verticalGradedMesh)
        build.add(self.meshesFigure)

        build.add(self.conservation)

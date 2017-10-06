from ninjaopenfoam import Case, GmtPlot, GmtPlotCopyCase

import os

class ArakawaKonor:
    def __init__(self):
        self.uniformLorenz = GmtPlotCopyCase(
                'arakawaKonor-uniform-lorenz',
                source='$atmostests_builddir',
                target='$builddir',
                plots=['src/thesis/cp/arakawaKonor/theta_diff.gmtdict'],
                files=['0/theta_diff', '172800/theta_diff'])

        uniformLorenzCase = Case('arakawaKonor-uniform-lorenz')

        self.initialThetaDiff = GmtPlot(
            'arakawaKonor-initial-theta_diff',
            plot='theta_diff',
            case=uniformLorenzCase,
            time=0,
            data=['0/theta_diff'])

        self.uniformLorenzThetaDiff = GmtPlot(
            'arakawaKonor-uniform-lorenz-theta_diff',
            plot='theta_diff',
            case=uniformLorenzCase,
            time=172800,
            data=['172800/theta_diff'])

    def outputs(self):
        return self.initialThetaDiff.outputs() + \
               self.uniformLorenzThetaDiff.outputs()

    def addTo(self, build):
        build.add(self.uniformLorenz)
        build.add(self.initialThetaDiff)
        build.add(self.uniformLorenzThetaDiff)

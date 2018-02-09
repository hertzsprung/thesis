from ninjaopenfoam import Case, Gnuplot
import os

class SchaerAdvectSmooth:
    def __init__(self):
        self.convergence = Gnuplot(
                'highOrderFit-schaerAdvectSmooth-convergence',
                output=os.path.join('thesis/highOrderFit/schaerAdvectSmooth/convergence'),
                plot=os.path.join('src/thesis/highOrderFit/schaerAdvectSmooth/convergence.plt'),
                data=[
                ])

    def outputs(self):
        return self.convergence.outputs()

    def addTo(self, build):
        build.add(self.convergence)

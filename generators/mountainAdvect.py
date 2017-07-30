from ninjaopenfoam import Gnuplot, LaTeXSubstitution, siunitx, Paths
import itertools
import os

class MountainAdvect:
    def __init__(self):
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
        return self.l2ByMountainHeight.outputs() \
                + self.maxdt.outputs() \
                + self.timesteps.outputs() \
                + self.unstableCourantNumber.outputs()

    def addTo(self, build):
        build.add(self.l2ByMountainHeight)
        build.add(self.maxdt)
        build.add(self.timesteps)
        build.add(self.unstableCourantNumber)

#!/bin/bash
set -e
set -a
source build.properties

ninja -C $atmostests_dir build/deformationSphere-mesh-hex-{4,8,9}/averageEquatorialSpacing.txt
ninja -C $atmostests_dir build/deformationSphere-gaussians-hex-8-cubicFit/{0,518400,1036800}/T
ninja -C $atmostests_dir build/deformationSphere-gaussians-{hex,cubedSphere}-{linearUpwind,cubicFit}-collated/1036800/l{2,inf}errorT.txt

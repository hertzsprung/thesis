#!/bin/bash
set -e
set -a
source build.properties

ninja -C $atmostests_dir build/deformationSphere-mesh-hex-{4,8,9}/averageEquatorialSpacing.txt
ninja -C $atmostests_dir build/deformationSphere-gaussians-hex-8-cubicFit/{0,518400,1036800}/T
ninja -C $atmostests_dir build/deformationSphere-{cosBells,gaussians}-{hex,cubedSphere}-{linearUpwind,cubicFit}-collated/1036800/l{2,inf}errorT.txt
ninja -C $atmostests_dir build/schaerAdvect-btf-{linearUpwind,cubicFit}-collated/10000/l{2,inf}errorT.txt
ninja -C $atmostests_dir build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{linearUpwind,cubicFit}-collated/10000/l2errorT.txt
ninja -C $atmostests_dir build/mountainAdvect-h0-{btf,cutCell,slantedCell}-1000-{0,3000,4000,5000,6000}m-linearUpwind/dt.txt
ninja -C $atmostests_dir build/mountainAdvect-maxdt-{btf,cutCell,slantedCell}-6000m-cubicFit-collated/{dt,co}.txt
ninja -C $atmostests_dir build/mountainAdvect-h0-slantedCell-1000-6000m-linearUpwind/co.txt

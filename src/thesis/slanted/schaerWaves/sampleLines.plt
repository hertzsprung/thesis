set term epslatex color size 6,4

set style data linespoints

set multiplot layout 2,3
#margins 0.1,0.95,0.1,0.9 spacing 0.15

set xrange [-0.1:0.1]
set yrange [0:1200]
set ylabel "$z$ (\\si{\\meter})" offset 3
set yzeroaxis

set xlabel "$\\theta$ (\\si{\\kelvin})" offset 0,0.5
set ytics format "% h"
set ylabel "$z$ (\\si{\\meter})" offset 3

set title "Sch\\\"{a}r waves BTF"
plot "`echo $atmostests_builddir`/schaerWaves-btf-300dz-cubicFit/18000/theta_diff.sampleLine.dat" using 2:1 notitle

unset ylabel
set title "Sch\\\"{a}r waves cut cells"
plot "`echo $atmostests_builddir`/schaerWaves-cutCell-300dz-cubicFit/18000/theta_diff.sampleLine.dat" using 2:1 notitle

set title "Sch\\\"{a}r waves slanted cells"
plot "`echo $atmostests_builddir`/schaerWaves-slantedCell-300dz-cubicFit/18000/theta_diff.sampleLine.dat" using 2:1 notitle

set ylabel "$z$ (\\si{\\meter})" offset 3
set title "Thermal transport BTF"
plot "`echo $atmostests_builddir`/thermalAdvect-btf-500dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-btf-300dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-btf-250dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-btf-200dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-btf-150dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-btf-125dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-btf-100dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{100}{\meter}', \
     "`echo $atmostests_builddir`/thermalAdvect-btf-75dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{75}{\meter}', \
     "`echo $atmostests_builddir`/thermalAdvect-btf-50dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{50}{\meter}'

unset ylabel
set title "Thermal transport cut cells"
plot "`echo $atmostests_builddir`/thermalAdvect-cutCell-500dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-300dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-250dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-200dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-150dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-125dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-100dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{100}{\meter}', \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-75dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{75}{\meter}', \
     "`echo $atmostests_builddir`/thermalAdvect-cutCell-50dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{50}{\meter}'

set title "Thermal transport slanted cells"
plot "`echo $atmostests_builddir`/thermalAdvect-slantedCell-500dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-300dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-250dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-200dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-150dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-125dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 notitle, \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-100dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{100}{\meter}', \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-75dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{75}{\meter}', \
     "`echo $atmostests_builddir`/thermalAdvect-slantedCell-50dz-cubicFit/18000/T_diff.sampleLine.dat" using 2:1 title '\SI{50}{\meter}'

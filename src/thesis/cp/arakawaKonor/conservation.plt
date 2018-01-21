set term epslatex color size 4.4,2.6

set style data lines

set xlabel "Time (hours)"
set ylabel "Total energy change" offset 1
set ytics format "$\\num{%2.1e}$"

set xtics 6

set yrange [-1e-3:3e-3]

#set key outside bottom center

set xrange [0:48]
plot "`echo $atmostests_builddir`/arakawaKonor-uniform-lorenz/energy.dat" using ($1/3600):5 lc 6 lw 2 title 'Lorenz', \
     "`echo $atmostests_builddir`/arakawaKonor-uniform-cp/energy.dat" using ($1/3600):5 lc 7 lw 2 title 'Generalised Charney--Phillips', \
     "`echo $atmostests_builddir`/arakawaKonor-horizontalGrading-lorenz/energy.dat" using ($1/3600):5 lc 6 dt 2 lw 2 notitle, \
     "`echo $atmostests_builddir`/arakawaKonor-horizontalGrading-cp/energy.dat" using ($1/3600):5 lc 7 dt 2 lw 2 notitle, \
     "`echo $atmostests_builddir`/arakawaKonor-verticalGrading-lorenz/energy.dat" using ($1/3600):5 lc 6 dt 3 lw 2 notitle, \
     "`echo $atmostests_builddir`/arakawaKonor-verticalGrading-cp/energy.dat" using ($1/3600):5 lc 7 dt 3 lw 2 notitle, \
     -1 lc rgbcolor "black" dt 1 lw 2 title 'Uniform mesh', \
     -1 lc rgbcolor "black" dt 2 lw 2 title 'Horizontally tilted mesh', \
     -1 lc rgbcolor "black" dt 3 lw 2 title 'Vertically tilted mesh'


#set term epslatex color size 3.2,2.6

set style data lines

set xlabel "Time (hours)"
set ylabel "Total energy change" offset 1
set ytics format "$\\num{%2.1e}$"

set xtics 6

set key outside bottom center

set xrange [0:48]
plot "`echo $atmostests_builddir`/arakawaKonor-uniform-lorenz/energy.dat" using ($1/3600):5 lc 6 lw 1.5 title 'Lorenz', \
     "`echo $atmostests_builddir`/arakawaKonor-uniform-cp/energy.dat" using ($1/3600):5 lc 7 lw 1.5 title 'Charney--Phillips', \
     "`echo $atmostests_builddir`/arakawaKonor-horizontalGrading-lorenz/energy.dat" using ($1/3600):5 lc 6 dt 2 lw 1.5 notitle, \
     "`echo $atmostests_builddir`/arakawaKonor-horizontalGrading-cp/energy.dat" using ($1/3600):5 lc 7 dt 2 lw 1.5 notitle



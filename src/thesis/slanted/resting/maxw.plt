set term epslatex color colortext size 5,3

set style data linespoints
set logscale y

set xlabel "Peak mountain height $h_0$ (\\si{\\kilo\\meter})"
set ylabel "$\\max(\\Mag{w})$ (\\si{\\meter\\per\\second})" offset 1

set xrange [0:8]
set yrange [0.0001:20]

set ytics format "$10^{%T}$"

set key inside bottom right

plot "`echo $atmostests_builddir`/resting-btf-cubicFit-collated/maxw.txt" using ($1/1000):($2) title 'BTF cubicFit', \
     "`echo $atmostests_builddir`/resting-sleve-cubicFit-collated/maxw.txt" using ($1/1000):($2) title 'SLEVE cubicFit', \
     "`echo $atmostests_builddir`/resting-cutCell-cubicFit-collated/maxw.txt" using ($1/1000):($2) title 'cutCell cubicFit', \
     "`echo $atmostests_builddir`/resting-slantedCell-cubicFit-collated/maxw.txt" using ($1/1000):($2) title 'slantedCell cubicFit', \
     "`echo $atmostests_builddir`/resting-btf-linearUpwind-collated/maxw.txt" using ($1/1000):($2) lc 1 dt 2 title 'BTF linearUpwind', \
     "`echo $atmostests_builddir`/resting-sleve-linearUpwind-collated/maxw.txt" using ($1/1000):($2) lc 2 dt 2 title 'SLEVE linearUpwind', \
     "`echo $atmostests_builddir`/resting-cutCell-linearUpwind-collated/maxw.txt" using ($1/1000):($2) lc 3 dt 2 title 'cutCell linearUpwind', \
     "`echo $atmostests_builddir`/resting-slantedCell-linearUpwind-collated/maxw.txt" using ($1/1000):($2) lc 4 dt 2 title 'slantedCell linearUpwind'

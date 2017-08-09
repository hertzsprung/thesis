set style data linespoints

set xlabel 'h_0 (m)'
set ylabel 'max(abs(w)) (ms-1)'

set yrange [0:1]

set multiplot layout 1,2

set key inside top left

set title 'meanw'
plot "`echo $atmostests_builddir`/resting-btf-cubicFit-collated/meanw.txt" using 1:2 title 'BTF cubicFit', \
     "`echo $atmostests_builddir`/resting-sleve-cubicFit-collated/meanw.txt" using 1:2 title 'SLEVE cubicFit', \
     "`echo $atmostests_builddir`/resting-cutCell-cubicFit-collated/meanw.txt" using 1:2 title 'cutCell cubicFit', \
     "`echo $atmostests_builddir`/resting-slantedCell-cubicFit-collated/meanw.txt" using 1:2 title 'slantedCell cubicFit', \
     "`echo $atmostests_builddir`/resting-btf-linearUpwind-collated/meanw.txt" using 1:2 lc 1 dt 2 title 'BTF linearUpwind', \
     "`echo $atmostests_builddir`/resting-sleve-linearUpwind-collated/meanw.txt" using 1:2 lc 2 dt 2 title 'SLEVE linearUpwind', \
     "`echo $atmostests_builddir`/resting-cutCell-linearUpwind-collated/meanw.txt" using 1:2 lc 3 dt 2 title 'cutCell linearUpwind', \
     "`echo $atmostests_builddir`/resting-slantedCell-linearUpwind-collated/meanw.txt" using 1:2 lc 4 dt 2title 'slantedCell linearUpwind'

set title 'maxw'
plot "`echo $atmostests_builddir`/resting-btf-cubicFit-collated/maxw.txt" using 1:2 notitle, \
     "`echo $atmostests_builddir`/resting-sleve-cubicFit-collated/maxw.txt" using 1:2 notitle, \
     "`echo $atmostests_builddir`/resting-cutCell-cubicFit-collated/maxw.txt" using 1:2 notitle, \
     "`echo $atmostests_builddir`/resting-slantedCell-cubicFit-collated/maxw.txt" using 1:2 notitle, \
     "`echo $atmostests_builddir`/resting-btf-linearUpwind-collated/maxw.txt" using 1:2 lc 1 dt 2 notitle, \
     "`echo $atmostests_builddir`/resting-sleve-linearUpwind-collated/maxw.txt" using 1:2 lc 2 dt 2 notitle, \
     "`echo $atmostests_builddir`/resting-cutCell-linearUpwind-collated/maxw.txt" using 1:2 lc 3 dt 2 notitle, \
     "`echo $atmostests_builddir`/resting-slantedCell-linearUpwind-collated/maxw.txt" using 1:2 lc 4 dt 2 notitle

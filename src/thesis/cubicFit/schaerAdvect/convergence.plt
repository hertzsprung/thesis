set term epslatex color size 5.6,5

set style data linespoints
set logscale
set format x "$10^{%L}$"
set format y "$10^{%L}$"

set key tmargin

set xrange [10000:100]
set yrange [1e-4:1]

set multiplot layout 2,2 margins 0.1, 0.95, 0.06, 0.8 spacing 0.15,0.12

set label "Horizontal velocity field" at screen 0.5,0.84 centre
set label "Terrain-following velocity field" at screen 0.5,0.41 centre

### l2

set label "(a)" at 8e3,3e-4

set ylabel "$\\ell_2$ error" offset 1.5
plot "`echo $atmostests_builddir`/schaerAdvect-btf-linearUpwind-collated/10000/l2errorT.txt" using 1:2 lc 1 dt 3 lw 2 pt 4 title 'BTF, linearUpwind', \
     "`echo $atmostests_builddir`/schaerAdvect-btf-cubicFit-collated/10000/l2errorT.txt" using 1:2 lc 1 pt 5 title 'BTF, cubicFit', \
     "`echo $atmostests_builddir`/schaerAdvect-cutCell-linearUpwind-collated/10000/l2errorT.txt" using 1:2 lc 2 dt 3 lw 2 pt 6 title 'Cut cells, linearUpwind', \
     "`echo $atmostests_builddir`/schaerAdvect-cutCell-cubicFit-collated/10000/l2errorT.txt" using 1:2 lc 2 pt 7 title 'Cut cells, cubicFit', \
     x * 5e-4 lc rgbcolor "black" dt 1 lw 1 notitle, \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 notitle,\
     x**2 * 1e-8 lc rgbcolor "black" dt 3 lw 3 notitle

### linf

unset label
set label "(b)" at 8e3,3e-4

set ylabel "$\\ell_\\infty$ error" offset 1.5
plot "`echo $atmostests_builddir`/schaerAdvect-btf-linearUpwind-collated/10000/linferrorT.txt" using 1:2 lc 1 dt 3 lw 2 pt 4 notitle, \
     "`echo $atmostests_builddir`/schaerAdvect-btf-cubicFit-collated/10000/linferrorT.txt" using 1:2 lc 1 pt 5 notitle, \
     "`echo $atmostests_builddir`/schaerAdvect-cutCell-linearUpwind-collated/10000/linferrorT.txt" using 1:2 lc 2 dt 3 lw 2 pt 6 notitle, \
     "`echo $atmostests_builddir`/schaerAdvect-cutCell-cubicFit-collated/10000/linferrorT.txt" using 1:2 lc 2 pt 7 notitle, \
     x * 5e-4 lc rgbcolor "black" dt 1 lw 1 title '1st order', \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 title '2nd order', \
     x**2 * 1e-8 lc rgbcolor "black" dt 3 lw 3 notitle

### l2

unset label
set label "(c)" at 8e3,3e-4

unset key

set xlabel "$\\Delta x$ (\\si{\\meter})" offset 0,0.5

set ylabel "$\\ell_2$ error" offset 1.5
plot "`echo $atmostests_builddir`/tfAdvect-btf-linearUpwind-collated/10000/l2errorT.txt" using 1:2 lc 1 dt 3 lw 2 pt 4 notitle, \
     "`echo $atmostests_builddir`/tfAdvect-btf-cubicFit-collated/10000/l2errorT.txt" using 1:2 lc 1 pt 5 notitle, \
     "`echo $atmostests_builddir`/tfAdvect-cutCell-linearUpwind-collated/10000/l2errorT.txt" using 1:2 lc 2 dt 3 lw 2 pt 6 notitle, \
     "`echo $atmostests_builddir`/tfAdvect-cutCell-cubicFit-collated/10000/l2errorT.txt" using 1:2 lc 2 pt 7 notitle, \
     x * 5e-4 lc rgbcolor "black" dt 1 lw 1 notitle, \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 notitle,\
     x**2 * 1e-8 lc rgbcolor "black" dt 3 lw 3 notitle

### linf

unset label
set label "(d)" at 8e3,3e-4

set ylabel "$\\ell_\\infty$ error" offset 1.5

plot "`echo $atmostests_builddir`/tfAdvect-btf-linearUpwind-collated/10000/linferrorT.txt" using 1:2 lc 1 dt 3 lw 2 pt 4 notitle, \
     "`echo $atmostests_builddir`/tfAdvect-btf-cubicFit-collated/10000/linferrorT.txt" using 1:2 lc 1 pt 5 notitle, \
     "`echo $atmostests_builddir`/tfAdvect-cutCell-linearUpwind-collated/10000/linferrorT.txt" using 1:2 lc 2 dt 3 lw 2 pt 6 notitle, \
     "`echo $atmostests_builddir`/tfAdvect-cutCell-cubicFit-collated/10000/linferrorT.txt" using 1:2 lc 2 pt 7 notitle, \
     x * 5e-4 lc rgbcolor "black" dt 1 lw 1 notitle, \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 notitle, \
     x**2 * 1e-8 lc rgbcolor "black" dt 3 lw 3 notitle

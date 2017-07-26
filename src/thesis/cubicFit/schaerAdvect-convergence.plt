set term epslatex color size 5.6,2.7

set style data linespoints
set logscale
set format x "$10^{%L}$"
set format y "$10^{%L}$"

set key tmargin

set xlabel "$\\Delta x$ (\\si{\\meter})" offset 0,0.5

set xrange [10000:100]
set yrange [1e-2:1]

set multiplot layout 1,2

### l2

set ylabel "$\\ell_2$ error" offset 1.5
plot "`echo $atmostests_builddir`/schaerAdvect-btf-linearUpwind-collated/10000/l2errorT.txt" using 1:2 lc 1 dt 3 lw 2 title 'linearUpwind', \
     "`echo $atmostests_builddir`/schaerAdvect-btf-cubicFit-collated/10000/l2errorT.txt" using 1:2 lc 1 title 'cubicFit', \
     x * 5e-4 lc rgbcolor "black" dt 1 lw 1 notitle, \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 notitle

### linf

set rmargin 4
set ylabel "$\\ell_\\infty$ error" offset 1.5
plot "`echo $atmostests_builddir`/schaerAdvect-btf-linearUpwind-collated/10000/linferrorT.txt" using 1:2 lc 1 dt 3 lw 2 notitle, \
     "`echo $atmostests_builddir`/schaerAdvect-btf-cubicFit-collated/10000/linferrorT.txt" using 1:2 lc 1 notitle, \
     x * 5e-4 lc rgbcolor "black" dt 1 lw 1 title '1st order', \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 title '2nd order'

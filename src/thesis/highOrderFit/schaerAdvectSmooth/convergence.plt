set term epslatex color size 5.6,2.8

set style data linespoints
set logscale
set format x "$10^{%L}$"
set format y "$10^{%L}$"

set key tmargin

set xrange [10000:100]
set yrange [1e-5:1]

set multiplot layout 1,2 margins 0.1, 0.95, 0.12, 0.73 spacing 0.15,0.12

### l2

set xlabel "$\\Delta x$ (\\si{\\meter})" offset 0,0.4
set ylabel "$\\ell_2$ error" offset 1.2

plot x**2 * 9e-9 lc rgbcolor 'black' dt 3 lw 3 notitle, \
     x**3 * 3e-10 lc rgbcolor 'black' dt (6,2) lw 2 notitle, \
     x**4 * 1e-14 lc rgbcolor 'black' dt 5 lw 2 notitle, \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-btf-cubicFit-collated/10000/l2errorT.txt" using 1:2 lc 1 pt 5 title 'BTF, cubicFit', \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-btf-highOrderFit-collated/10000/l2errorT.txt" using 1:2 lc 1 pt 4 dt 4 lw 2 title 'BTF, highOrderFit', \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-cutCell-cubicFit-collated/10000/l2errorT.txt" using 1:2 lc 2 pt 7 title 'Cut cells, cubicFit', \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-cutCell-highOrderFit-collated/10000/l2errorT.txt" using 1:2 lc 2 pt 6 dt 4 lw 2 title 'Cut cells, highOrderFit'

### linf

set ylabel "$\\ell_\\infty$ error" offset 1.5

plot x**2 * 9e-9 lc rgbcolor 'black' dt 3 lw 3 title "2nd order", \
     x**3 * 3e-10 lc rgbcolor 'black' dt (6,2) lw 2 title "3rd order", \
     x**4 * 1e-14 lc rgbcolor 'black' dt 5 lw 2 title "4th order", \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-btf-cubicFit-collated/10000/linferrorT.txt" using 1:2 lc 1 pt 5 notitle, \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-btf-highOrderFit-collated/10000/linferrorT.txt" using 1:2 lc 1 pt 4 dt 4 lw 2 notitle, \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-cutCell-cubicFit-collated/10000/linferrorT.txt" using 1:2 lc 2 pt 7 notitle, \
     "`echo $atmostests_builddir`/schaerAdvectSmooth-cos4-cutCell-highOrderFit-collated/10000/linferrorT.txt" using 1:2 lc 2 pt 6 dt 4 lw 2 notitle

unset multiplot

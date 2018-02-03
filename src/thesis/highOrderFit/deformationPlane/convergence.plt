set term epslatex color size 5.6,2.8

set style data linespoints
set logscale
set format x "$10^{%L}$"
set format y "$10^{%L}$"

set key tmargin

set xrange [10000:100]
set yrange [1e-4:1]

set multiplot layout 1,2 margins 0.1, 0.95, 0.1, 0.75 spacing 0.15,0.12

### l2

set label "(a)" at 8e3,3e-4

set xlabel "$\\Delta x$ (\\si{\\meter})" offset 0,0.5
set ylabel "$\\ell_2$ error" offset 1.2

plot x * 5e-4 lc rgbcolor "black" dt 1 lw 1 notitle, \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 notitle, \
     x**3 * 1e-10 lc rgbcolor "black" dt (6,2) lw 2 notitle, \
     x**4 * 1e-14 lc rgbcolor "black" dt 5 lw 2 notitle 

### linf

unset label
set label "(b)" at 8e3,3e-4

set ylabel "$\\ell_\\infty$ error" offset 1.5

plot x * 5e-4 lc rgbcolor "black" dt 1 lw 1 title '1st order', \
     x**2 * 2e-7 lc rgbcolor "black" dt 3 lw 3 title '2nd order', \
     x**3 * 1e-10 lc rgbcolor "black" dt (6,2) lw 2 title '3rd order', \
     x**4 * 1e-14 lc rgbcolor "black" dt 5 lw 2 title '4th order'

unset multiplot

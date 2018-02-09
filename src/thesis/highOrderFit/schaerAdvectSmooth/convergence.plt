set term epslatex color size 5.6,2.8

set style data linespoints
set logscale
set format x "$10^{%L}$"
set format y "$10^{%L}$"

set key tmargin

set xrange [10000:100]
set yrange [1e-4:1]

set multiplot layout 1,2 margins 0.1, 0.95, 0.12, 0.73 spacing 0.15,0.12

### l2

set xlabel "$\\Delta x$ (\\si{\\meter})" offset 0,0.4
set ylabel "$\\ell_2$ error" offset 1.2

plot x**2 * 8e-8 lc rgbcolor 'black' dt 3 lw 3 title "2nd order", \
     x**2 * 9e-9 lc rgbcolor 'black' dt 3 lw 3 notitle, \
     x**3 * 3e-10 lc rgbcolor 'black' dt (6,2) lw 2 title "3rd order", \
     x**4 * 1e-14 lc rgbcolor 'black' dt 5 lw 2 title "4th order"

### linf

set ylabel "$\\ell_\\infty$ error" offset 1.5

plot x**2 * 8e-8 lc rgbcolor 'black' dt 3 lw 3 notitle, \
     x**2 * 9e-9 lc rgbcolor 'black' dt 3 lw 3 notitle, \
     x**3 * 3e-10 lc rgbcolor 'black' dt (6,2) lw 2 notitle, \
     x**4 * 1e-14 lc rgbcolor 'black' dt 5 lw 2 notitle

unset multiplot

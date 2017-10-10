set term epslatex color colortext size 5.2,2.5

set style data lines
set logscale y

set xlabel "$t$ (hours)" offset 0,0.4
set ylabel "$\\mathrm{max}(\\Mag{w})$ (\\si{\\meter\\per\\second})" offset 2

set xrange [0:6]
set yrange [1e-5:20]

set ytics offset 0.5 format "$10^{%T}$"

set multiplot layout 1,2 margins 0.08, 0.98, 0.12, 0.94 spacing 0.12,0.12

# t

unset key
set label "(a)" at 0.2,5
set label "BTF" at 0.8,3e-1
set label "SLEVE" at 0.8,1.5e-2
set label "Cut cells" at 0.8,6e-4
set label "Slanted cells" at 0.8,5e-5

plot "`echo $atmostests_builddir`/resting-btf-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 1 lw 2 title 'cubicFit BTF', \
     "`echo $atmostests_builddir`/resting-sleve-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 4 lw 2 title 'cubicFit SLEVE', \
     "`echo $atmostests_builddir`/resting-cutCell-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 2 lw 2 title 'cubicFit cutCell', \
     "`echo $atmostests_builddir`/resting-slantedCell-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 3 lw 2 title 'cubicFit slantedCell'

# h0

set style data linespoints
set key inside bottom right
set xrange [0:6]
set xlabel "Peak mountain height $h_0$ (\\si{\\kilo\\meter})"
set ylabel "$\\max(\\Mag{w})$ (\\si{\\meter\\per\\second})" offset 2
unset label
set label "(b)" at 0.2,5

plot "`echo $atmostests_builddir`/resting-btf-cubicFit-collated/maxw.txt" using ($1/1000):($2) lc 1 lw 2 pt 5 title 'BTF', \
     "`echo $atmostests_builddir`/resting-sleve-cubicFit-collated/maxw.txt" using ($1/1000):($2) lc 4 lw 2 pt 13 ps 1.5 title 'SLEVE', \
     "`echo $atmostests_builddir`/resting-cutCell-cubicFit-collated/maxw.txt" using ($1/1000):($2) lc 2 lw 2 pt 7 title 'cutCell', \
     "`echo $atmostests_builddir`/resting-slantedCell-cubicFit-collated/maxw.txt" using ($1/1000):($2) lc 3 lw 2 pt 9 ps 1.5 title 'slantedCell'

unset multiplot

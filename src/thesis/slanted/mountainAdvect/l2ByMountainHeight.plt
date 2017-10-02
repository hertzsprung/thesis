set term epslatex color colortext size 4.5,3

set xrange [0:10]
set yrange [2e-3:0.3]

set style data linespoints
set logscale y

set xlabel "Peak mountain height $h_0$ (\\si{\\kilo\\meter})"
set ylabel "$\\ell_2$ error" offset 3

set label "\\textit{BTF, linearUpwind}" at 6.2,0.074 textcolor rgb "dark-violet"
set label "BTF, cubicFit" at 6.2,0.04 textcolor rgb "dark-violet"
set label "\\textit{Cut cells, linearUpwind}" at 6.2,0.15 textcolor rgb "#009e73"
set label "Cut cells, cubicFit" at 6.2,0.055 textcolor rgb "#009e73"
set label "\\textit{Slanted cells, linearUpwind}" at 5.2,0.22 textcolor rgb "#1a8acb"
set label "Slanted cells, cubicFit" at 6.2,0.097 textcolor rgb "#1a8acb"

unset key

plot "`echo $atmostests_builddir`/mountainAdvect-h0-btf-1000-linearUpwind-collated/10000/l2errorT.txt" using ($1/1000):($2) lc 1 lw 2 dt 2 ps 1.5 pt 4, \
     "`echo $atmostests_builddir`/mountainAdvect-h0-btf-1000-cubicFit-collated/10000/l2errorT.txt" using ($1/1000):($2) lc 1 lw 2 dt 1 ps 1.5 pt 5, \
     "`echo $atmostests_builddir`/mountainAdvect-h0-cutCell-1000-linearUpwind-collated/10000/l2errorT.txt" using ($1/1000):($2) lc 2 lw 2 dt 2 ps 1.5 pt 6, \
     "`echo $atmostests_builddir`/mountainAdvect-h0-cutCell-1000-cubicFit-collated/10000/l2errorT.txt" using ($1/1000):($2) lc 2 lw 2 dt 1 ps 1.5 pt 7, \
     "`echo $atmostests_builddir`/mountainAdvect-h0-slantedCell-1000-linearUpwind-collated/10000/l2errorT.txt" using ($1/1000):($2) lc 3 lw 2 dt 2 ps 1.5 pt 8, \
     "`echo $atmostests_builddir`/mountainAdvect-h0-slantedCell-1000-cubicFit-collated/10000/l2errorT.txt" using ($1/1000):($2) lc 3 lw 2 dt 1 ps 1.5 pt 9

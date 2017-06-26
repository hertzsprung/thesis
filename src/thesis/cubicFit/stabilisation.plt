set term epslatex color colortext size 6,2.2

set xrange [-4:1]
set yrange [0:4]

set xzeroaxis lt -1
set yzeroaxis lt -1
unset border
set xtics axis
set ytics axis 1,1

set xlabel "$x$"
set ylabel "$\\phi$" offset 15.7,6.4 rotate by 0

set multiplot 	layout 1,3  \
		margins 0,0.95,0.15,0.92 \
		spacing 0.05,0.1

centralQuad(x) = 1.7492178992983982 + 0.13068611504740824 * x + 0.18146888996940846 * x**2
upwindQuad(x) = 1.714040750993586 + 0.0825285803352164 * x + 0.16848849229653406 * x**2
cubic(x) = 1.235260039951814 + 0.25819808959890267 * x + 1.1253490271335935 * x ** 2 + 0.30241086533520734 * x**3

set label "(a)" at -4,4

set label "0.127" at -2.8,2.7 offset char -4,0 
set label "-0.958" at -1.6,2.4 offset char -4.7,0 
set label "-0.352" at -1.2,2.2 offset char 0.3,char 0.6 
set label "\\textit{1.822}" at -1.1,1.8 offset char -4,char -0.5 textcolor lt 7
set label "0.361" at 0.4,1.9 offset char 1.5,0 

plot cubic(x) lc -1 lw 1.7 notitle, \
  "cubic.dat" using 1:2:3 with points ps 1.5 lc variable notitle

unset label
set label "(b)" at -3,4

set label "-0.096" at -2.8,2.7 offset char -4.7,0 
set label "-0.021" at -1.6,2.4 offset char -2.5,char 0.7 
set label "-0.006" at -1.2,2.2 offset char 0.3,char 0.6 
set label "0.62" at -1,1.8 offset char -4,char -0.5 
set label "\\textit{0.502}" at 0.4,1.9 offset char 1.5,char -0.3 textcolor lt 7


plot centralQuad(x) lc -1 lw 1.7 notitle, \
  "centralQuad.dat" using 1:2:3 with points ps 1.5 lc variable notitle

unset label
set label "(c)" at -3,4

set label "-0.081" at -2.8,2.7 offset char -4.7,0
set label "-0.082" at -1.6,2.4 offset char -2.5,char 0.7
set label "-0.033" at -1.2,2.2 offset char 0.3,char 0.6 
set label "0.703" at -1,1.8 offset char -4,char -0.5 
set label "0.493" at 0.62,1.9 offset char -1.5,char 0.8 

plot upwindQuad(x) lc -1 lw 1.7 notitle, \
  "cubic.dat" using 1:2 with points lc -1 ps 1.5 notitle

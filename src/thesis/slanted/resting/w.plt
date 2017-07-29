set style data lines
set xrange [0:6]
set logscale y
set xlabel "$t$ (hours)" offset 0,1
set ylabel "$\\mathrm{max}(w)$ (\\si{\\meter\\per\\second})" offset 4
set xtics offset 0,0.5
set ytics offset 0.5 format "$10^{%T}$"

set key outside

plot "/home/jshaw/AtmosTests/build/resting-btf-1000m-linearUpwind/energy.dat" using ($1/3600):6 title 'linUp BTF 1000m', \
     "/home/jshaw/AtmosTests/build/resting-sleve-1000m-linearUpwind/energy.dat" using ($1/3600):6 title 'linUp SLEVE 1000m', \
     "/home/jshaw/AtmosTests/build/resting-cutCell-1000m-linearUpwind/energy.dat" using ($1/3600):6 title 'linUp cutCell 1000m', \
     "/home/jshaw/AtmosTests/build/resting-slantedCell-1000m-linearUpwind/energy.dat" using ($1/3600):6 title 'linUp slantedCell 1000m', \
     "/home/jshaw/AtmosTests/build/resting-btf-2000m-linearUpwind/energy.dat" using ($1/3600):6 lc 1 dt 2 title 'linUp BTF 2000m', \
     "/home/jshaw/AtmosTests/build/resting-sleve-2000m-linearUpwind/energy.dat" using ($1/3600):6 lc 2 dt 2 title 'linUp SLEVE 2000m', \
     "/home/jshaw/AtmosTests/build/resting-cutCell-2000m-linearUpwind/energy.dat" using ($1/3600):6 lc 3 dt 2 title 'linUp cutCell 2000m', \
     "/home/jshaw/AtmosTests/build/resting-slantedCell-2000m-linearUpwind/energy.dat" using ($1/3600):6 lc 4 dt 2 title 'linUp slantedCell 2000m', \
     "/home/jshaw/AtmosTests/build/resting-btf-3000m-linearUpwind/energy.dat" using ($1/3600):6 lc 1 dt 3 title 'linUp BTF 3000m', \
     "/home/jshaw/AtmosTests/build/resting-sleve-3000m-linearUpwind/energy.dat" using ($1/3600):6 lc 2 dt 3 title 'linUp SLEVE 3000m', \
     "/home/jshaw/AtmosTests/build/resting-cutCell-3000m-linearUpwind/energy.dat" using ($1/3600):6 lc 3 dt 3 title 'linUp cutCell 3000m', \
     "/home/jshaw/AtmosTests/build/resting-slantedCell-3000m-linearUpwind/energy.dat" using ($1/3600):6 lc 4 dt 3 title 'linUp slantedCell 3000m', \
     "/home/jshaw/AtmosTests/build/resting-btf-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 1 lw 2 title 'cubicFit BTF 1000m', \
     "/home/jshaw/AtmosTests/build/resting-sleve-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 2 lw 2 title 'cubicFit SLEVE 1000m', \
     "/home/jshaw/AtmosTests/build/resting-cutCell-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 3 lw 2 title 'cubicFit cutCell 1000m', \
     "/home/jshaw/AtmosTests/build/resting-slantedCell-1000m-cubicFit/energy.dat" using ($1/3600):6 lc 4 lw 2 title 'cubicFit slantedCell 1000m', \
     "/home/jshaw/AtmosTests/build/resting-btf-2000m-cubicFit/energy.dat" using ($1/3600):6 lc 1 lw 2 dt 2 title 'cubicFit BTF 2000m', \
     "/home/jshaw/AtmosTests/build/resting-sleve-2000m-cubicFit/energy.dat" using ($1/3600):6 lc 2 lw 2 dt 2 title 'cubicFit SLEVE 2000m', \
     "/home/jshaw/AtmosTests/build/resting-cutCell-2000m-cubicFit/energy.dat" using ($1/3600):6 lc 3 lw 2 dt 2 title 'cubicFit cutCell 2000m', \
     "/home/jshaw/AtmosTests/build/resting-slantedCell-2000m-cubicFit/energy.dat" using ($1/3600):6 lc 4 lw 2 dt 2 title 'cubicFit slantedCell 2000m', \
     "/home/jshaw/AtmosTests/build/resting-btf-3000m-cubicFit/energy.dat" using ($1/3600):6 lc 1 lw 2 dt 3 title 'cubicFit BTF 3000m', \
     "/home/jshaw/AtmosTests/build/resting-sleve-3000m-cubicFit/energy.dat" using ($1/3600):6 lc 2 lw 2 dt 3 title 'cubicFit SLEVE 3000m', \
     "/home/jshaw/AtmosTests/build/resting-cutCell-3000m-cubicFit/energy.dat" using ($1/3600):6 lc 3 lw 2 dt 3 title 'cubicFit cutCell 3000m', \
     "/home/jshaw/AtmosTests/build/resting-slantedCell-3000m-cubicFit/energy.dat" using ($1/3600):6 lc 4 lw 2 dt 3 title 'cubicFit slantedCell 3000m'

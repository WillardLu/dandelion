# 博客园，繁星间漫步，陆巍的博客
from pylab import *

def DrawTest():
    figure(figsize=(4,3))
    x = linspace(0, 4, 1001)
    plot(x, 2*sin(2*pi*x/4))
    xlabel('$x$ (m)')
    ylabel('$y$ (m)')
    grid(True)
    savefig('draw_test.png', bbox_inches='tight')
    return ""
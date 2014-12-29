from numpy import array, pi, sin, linspace
from matplotlib.pyplot import plot, scatter

a = array([1,2,3])

# matplotlib 
# http://matplotlib.org/

x = linspace(0, 2*pi,50)
y = sin(x)
plot(x,y)

# red, dot-dash, triangles
plot(x, sin(x), 'r-^')
plot(x, sin(x), 'b-o',
     x, sin(2*x), 'r-^')
     
# Scatter plots

# simple scatter plot
x = linspace (0, 2*pi, 50)
y = sin(x)
scatter(x,y)

# coloar mapped Scatter plot
# Marker size/color set with data
x = rand(200)
y = rand(200)
size = rand(200)*30
color = rand(200)
scatter(x, y, size, color)
colorbar()
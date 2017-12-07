import numpy
import math

# numpy arrays are much more efficient than python lists
a = ((1,2,3), (3,4,5))
numpy_array = numpy.array(a)
print(numpy_array*2)

numpy_array = numpy.array([9,87,7])
print(numpy_array+10)
print(numpy.sqrt(numpy_array))

print(numpy.cos(numpy_array))
x = numpy.array([9,87,7])
y = numpy.array([10,13,89])

print(x-y)
m = numpy.matrix([x, y])
print(m)
print(m.T) # Transform

grid1 = numpy.zeros(shape=(10,10), dtype=float)
grid2 = numpy.ones(shape=(10,10), dtype=float)

print(grid1)
print(grid2)

print(grid1[1]+10)
print(grid2[:,2]*2)

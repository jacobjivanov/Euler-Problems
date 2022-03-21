# A firecracker explodes at a height of 100 m above level 
# ground. It breaks into a large number of very small 
# fragments, which move in every direction; all of them 
# have the same initial velocity of 20 m/s.

# We assume that the fragments move without air 
# resistance, in a uniform gravitational field 
# with g = 9.81 m/s^2.

# Find the volume (in m3) of the region through which the 
# fragments move before reaching the ground. Give your 
# answer rounded to four decimal places.


# This problem becomes much simpler if we evaluate it as a 2D area, then 
# revolve it to find the volume.

# See for t(theta), total time aloft vs initial angle
# https://www.desmos.com/calculator/xfh1bkwo8o

import numpy as np
r = 0 # the fragment path region will  be symmetric on the xz-plane at any y 
y = 0 # the y-axis will be defined as vertical

# Solved mathematically.
# Answer: 1856532.8455
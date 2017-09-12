# a quick hello-world program to try to learn about git and github

N = 6.0
if N % 2.0 == 0.0:
    print "Hello world! This number is even"

if N % 2.0 != 0.0:
    print "Hello world! this number is odd"

import numpy as np

print "2 to the power of this number is", np.power(2, N)

print "here is a random square matrix of size", int(N)

print np.random.rand(int(N), int(N))

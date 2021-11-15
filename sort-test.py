import numpy as numpy
import time as time

print("STARTED")

multiple = 100000000

data = numpy.random.rand(multiple)

tic = time.perf_counter()

sorted = numpy.sort(data, kind = "stable")

toc = time.perf_counter()

print(f"in {toc - tic:0.4f} seconds")

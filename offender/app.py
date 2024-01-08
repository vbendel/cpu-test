#!/usr/bin/env python3
import numpy as np
import os
from time import perf_counter

a = 2 * np.random.rand(50, 50) - 1
num_threads = int(os.environ.get('OMP_NUM_THREADS', -1))

def mul():
    t = perf_counter()
    a@a@a@a@a@a@a@a@a@a@a@a@a
    #print(f'{num_threads:3d} threads: {perf_counter() - t:6.2f} sec.')


while True:
    mul()

#!/usr/bin/env python3

from datetime import datetime
from time import perf_counter
import numpy as np


STAT_REPORT = 10


def main():

    stats = []

    a = 2 * np.random.rand(5000, 5000) - 1

    while True:
        for i in range(0, STAT_REPORT):
            t_0 = perf_counter()
            a@a
            t_1 = perf_counter()
            stats.append(t_1 - t_0)
        stats = sorted(stats)
        sum_var = sum(stats)
        print(f'{datetime.now()}: sum={sum_var:.6f} avg={sum_var/STAT_REPORT:.6f} max={stats[-1]:.6f} min={stats[0]:.6f} median={stats[STAT_REPORT//2]:.6f} p90={stats[-2]:.6f}')
        print(f'{stats}')
        stats.clear()


if __name__ == "__main__":
    main()
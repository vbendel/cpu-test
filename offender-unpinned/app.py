#!/usr/bin/env python3

from datetime import datetime
from time import perf_counter
import numpy as np


STAT_REPORT = 10

stats_global = {
    "sum": 0,
    "cnt": 0,
    "max": float("-inf"),
    "min": float("inf"),
}


def account_run(time: int):
    global stats_global
    stats_global["sum"] += time
    stats_global["cnt"] += 1
    if time > stats_global["max"]:
        stats_global["max"] = time
    if time < stats_global["min"]:
        stats_global["min"] = time


def main():
    global stats_global

    a = 2 * np.random.rand(5000, 5000) - 1

    while True:
        stats_run = []
        for i in range(0, STAT_REPORT):
            t_0 = perf_counter()
            a @ a @ a @ a @ a @ a @ a @ a @ a @ a @ a @ a @ a
            t_1 = perf_counter()
            time = t_1 - t_0
            stats_run.append(time)
            account_run(time)
            print(f"Multiply run: {stats_run[-1]:.6f}")
        stats = sorted(stats_run)
        stats_run.clear()
        sum_var = sum(stats)
        print(f'{datetime.now()}')
        print(
            'Last batch: ' +
            f'sum={sum_var:.6f} ' +
            f'avg={sum_var/STAT_REPORT:.6f} ' +
            f'max={stats[-1]:.6f} ' +
            f'min={stats[0]:.6f} ' +
            f'median={stats[STAT_REPORT//2]:.6f} ' +
            f'p90={stats[-2]:.6f}'
        )
        print(
            'Global stats: ' +
            f'sum={stats_global["sum"]:.6f} ' +
            f'cnt={stats_global["cnt"]} ' +
            f'avg={stats_global["sum"]/stats_global["cnt"]:.6f} ' +
            f'max={stats_global["max"]} ' +
            f'min={stats_global["min"]}'
        )


if __name__ == "__main__":
    main()

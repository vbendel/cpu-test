import os
import time
from functools import wraps

START = int(os.getenv("START", "100000"))
END = int(os.getenv("END", "900000"))


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            write_output(str(end_time - start_time))

    return wrapper

@calculate_time
def find_primes(start, end):
        primes = []
        for i in range(start, end + 1):
            if is_prime(i):
                primes.append(i)
        return primes


def write_output(total_time: str):
    file = open("result.txt", "w")
    file.write(total_time)
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"{current_time} {total_time}")
    file.close()

if __name__ == '__main__' :
    find_primes (START, END)

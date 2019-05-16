from dis import dis
from timeit import timeit
from time import sleep
import time


def sleep_sleep():
    x = sleep(1)

    return x


def sleep_time():
    x = time.sleep(1)

    return x


timeit('sleep_sleep()', number=100000)
timeit('sleep_time()', number=100000)

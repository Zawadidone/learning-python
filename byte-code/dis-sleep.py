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
sl


dis(sleep_sleep)
dis(sleep_time)

timeit('sleep_sleep()')
timeit('sleep_time()')

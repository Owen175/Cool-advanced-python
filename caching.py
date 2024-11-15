import functools
import random

@functools.lru_cache(maxsize=50)
def factorial(x):
    if x == 1:
        return x
    else:
        return factorial(x-1) * x


[print(factorial(100)) for i in range(100)]

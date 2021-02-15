from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
print(fib(10))

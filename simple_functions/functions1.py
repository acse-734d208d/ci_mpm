from functools import cache

__all__ = ['my_sum', 'factorial', 'my_sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


def my_sin(x):
    print(x)
    n = 80
    terms = []
    for i in range(n):
        term = ((-1)**i * x**(i*2+1) / factorial(i*2+1))
        terms.append(term)
    return my_sum(terms)

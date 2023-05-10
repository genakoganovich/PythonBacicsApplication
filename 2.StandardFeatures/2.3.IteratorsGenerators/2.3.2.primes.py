import itertools


def gen_int():
    i = 1
    while True:
        i += 1
        yield i


def count_divisors(value):
    count = 0
    for i in range(1, value + 1):
        if value % i == 0:
            count += 1
    return count


def primes():
    for i in gen_int():
        if count_divisors(i) == 2:
            yield i


def test():
    assert list(itertools.takewhile(lambda x: x <= 31, primes())) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


test()

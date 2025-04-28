import random
import functools

random.seed(42)

import pygon
from pygon import get_generator

edge = get_generator("edge")

def random_gen(n, m, pref=1, suf=1, inc=None):
    a = random.choices(range(1000000001), k=n)
    b = random.choices(range(1000000001), k=m)
    assert pref <= n and suf <= m
    a[:pref] = sorted(a[:pref])
    b[-suf:] = sorted(b[-suf:])
    if inc is not None:
        assert inc[0] <= pref and inc[1] <= suf
        c = sorted(a[:inc[0]] + b[-inc[1]:])
        a[:inc[0]] = c[:inc[0]]
        b[-inc[1]:] = c[-inc[1]:]
    return {"n": n, "m": m, "a": a, "b": b}

def test_writer(n, m, a, b, write):
    assert n == len(a) and m == len(b)
    write(n)
    write(*a, sep=' ')
    write(m)
    write(*b, sep=' ')

def generator(out, func, **params):
    writer = functools.partial(print, file=out)
    data = func(**params)
    test_writer(**data, write=writer)

problem = pygon.create_problem(
    source_code=r"E:\Coding\Competitive\Mega Sync\Nhat\PTNK\Nang khieu 2023\MARBLE.cpp",
    flags=["-O2"],
    output_dir=r"E:\Coding\Competitive\Mega Sync\Nhat\PTNK\Nang khieu 2023",
    generator=generator,
    test_params=[
        {"n": 1, "m": 1, "func": random_gen},
        {"n": 123, "m": 1, "func": random_gen},
        {"n": 5000, "m": 123, "pref": 10, "suf": 20, "inc": (5, 5), "func": random_gen},
        {"n": 5000, "m": 5000, "pref": 1000, "suf": 1000, "inc": (100, 100), "func": random_gen},
        {"n": 5000, "m": 5000, "pref": 5000, "suf": 4900, "inc": (2000, 1000), "func": random_gen},

        {"n": 3, "m": 92185, "pref": 2, "suf": 92185, "inc": (2, 20000), "func": random_gen},
        {"n": 99189, "m": 12345, "pref": 123, "suf": 11000, "inc": (60, 10000), "func": random_gen},
        {"n": 98765, "m": 100000, "pref": 23456, "suf": 12345, "inc": (10000, 10000), "func": random_gen},
        {"n": 100000, "m": 100000, "pref": 100000, "suf": 99999, "inc": (99000, 99000), "func": random_gen},
        {"n": 100000, "m": 100000, "pref": 12345, "suf": 100000, "inc": (10000, 90000), "func": random_gen},
    ],
)

problem.generate()
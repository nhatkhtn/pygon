import random
import functools

random.seed(42)

import pygon
from pygon import get_generator

edge = get_generator("edge")

def random_gen(n, m, w):
    transactions = [
        edge(n, w) for _ in range(m)
    ]
    return {"n": n, "m": m, "trans": transactions}
    
def all_same(n, w):
    trans = []
    assert n % 2 == 0
    halfn = n // 2
    for i in range(halfn):
        trans.append((i + 1, halfn + i + 1, w))
        trans.append((i + 1, n - i, w))
    return {"n": n, "m": len(trans), "trans": trans}

def test_writer(n, m, trans, write):
    write(n, m)
    assert m == len(trans)
    for x, y, w in trans:
        write(x, y, w)

def generator(out, func, **params):
    writer = functools.partial(print, file=out)
    data = func(**params)
    test_writer(**data, write=writer)

problem = pygon.create_problem(
    source_code=r"E:\Coding\Competitive\Mega Sync\Nhat\Tin hoc tre\2022\change.cpp",
    flags=["-O2"],
    output_dir=r"E:\Coding\Competitive\Mega Sync\Nhat\Tin hoc tre\2022",
    generator=generator,
    test_params=[
        {"n": 4, "m": 10, "w": 2, "func": random_gen},
        {"n": 4, "m": 10, "w": 2, "func": random_gen},
        {"n": 8, "m": 20, "w": 2, "func": random_gen},
        {"n": 10, "m": 10000, "w": 2, "func": random_gen},
        {"n": 10, "m": 10000, "w": 1000000, "func": random_gen},
        {"n": 10,             "w": 1000000, "func": all_same},

        {"n": 16, "m": 7, "w": 10, "func": random_gen},
        {"n": 16, "m": 100000, "w": 10, "func": random_gen},
        {"n": 16, "m": 100000, "w": 8, "func": random_gen},
        {"n": 16, "m": 100000, "w": 1000, "func": random_gen},
        {"n": 16, "m": 100000, "w": 10000, "func": random_gen},
        {"n": 16, "m": 100000, "w": 20, "func": random_gen},
        {"n": 16, "m": 100000, "w": 100, "func": random_gen},
        {"n": 16, "m": 100000, "w": 4, "func": random_gen},
        {"n": 16, "m": 100000, "w": 1000000, "func": random_gen},
        {"n": 16,              "w": 1000000, "func": all_same},

        {"n": 20, "m": 100000, "w": 10, "func": random_gen},
        {"n": 20, "m": 100000, "w": 1, "func": random_gen},
        {"n": 20, "m": 100000, "w": 2, "func": random_gen},
        {"n": 20,              "w": 1000000, "func": all_same},
    ],
)

problem.generate()
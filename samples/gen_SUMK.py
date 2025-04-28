import random
import functools

random.seed(42)

import pygon
from pygon import get_generator

edge = get_generator("edge")

def random_gen(n, k, low=0, high=100):
    a = random.choices(range(low, high + 1), k=n)
    return {"n": n, "k": k, "a": a}
    
def test_writer(n, k, a, write):
    write(n)
    assert n == len(a)
    write(*a, sep=' ')
    write(k)

def generator(out, func, **params):
    writer = functools.partial(print, file=out)
    data = func(**params)
    test_writer(**data, write=writer)

problem = pygon.create_problem(
    source_code=r"C:\Nhat\Workspace\PTNK\SUMK.cpp",
    flags=["-O2"],
    output_dir=r"C:\Nhat\Workspace\PTNK",
    generator=generator,
    test_params=[
        {"n": 1, "k": 1, "low": 1,  "high": 1,  "func": random_gen},
        {"n": 4, "k": 6,            "high": 3,  "func": random_gen},
        {"n": 80, "k": 3,           "high": 3,  "func": random_gen},
        {"n": 80, "k": 20,                      "func": random_gen},

        {"n": 100, "k": 1,      "high": 1,      "func": random_gen},
        {"n": 800, "k": 1260,   "high": 10,     "func": random_gen},
        {"n": 800, "k": 360360,                 "func": random_gen},
        {"n": 800, "k": 25200,  "high": 7,      "func": random_gen},

        {"n": 8000, "k": 1000000,   "low": 100, "func": random_gen},
        {"n": 7997, "k": 360360,    "low": 50,  "func": random_gen},
    ],
)

problem.generate()
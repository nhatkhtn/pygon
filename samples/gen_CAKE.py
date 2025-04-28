import random
import functools

random.seed(41)

import pygon
from pygon import get_generator

edge = get_generator("edge")

def random_gen(m, n, k):
    s = set()
    assert k * 4 <= n * m
    for _ in range(k * 4):
        while True:
            x = random.randint(1, m)
            y = random.randint(1, n)
            if (x, y) not in s:
                s.add((x, y))
                break
                    
    return {"m": m, "n": n, "k": k, "a": list(s)}
    
def test_writer(n, m, k, a, write):
    assert len(a) == k * 4
    write(m, n, k)
    for x in a:
        write(*x)

def generator(out, func, **params):
    writer = functools.partial(print, file=out)
    data = func(**params)
    test_writer(**data, write=writer)

problem = pygon.create_problem(
    source_code=r"C:\Nhat\Workspace\PTNK\CAKE.cpp",
    flags=["-O2"],
    output_dir=r"C:\Nhat\Workspace\PTNK",
    generator=generator,
    test_params=[
        {"n": 5, "m": 100000, "k": 1, "func": random_gen},
        {"n": 99994, "m": 123, "k": 1, "func": random_gen},
        {"n": 100000, "m": 100000, "k": 1, "func": random_gen},

        {"n": 14, "m": 4000, "k": 10, "func": random_gen},
        {"n": 3994, "m": 1234, "k": 100, "func": random_gen},
        {"n": 3994, "m": 4000, "k": 1000, "func": random_gen},

        {"n": 99994, "m": 100000, "k": 20, "func": random_gen},
        {"n": 99994, "m": 100000, "k": 1000, "func": random_gen},
        {"n": 99994, "m": 100000, "k": 10000, "func": random_gen},
        {"n": 100000, "m": 100000, "k": 50000, "func": random_gen},
    ],
)

def regen_when_zero(fin, fout):
    # returns true if the test has to be re-generated
    m, n, k = [int(x) for x in fin.readline().strip().split()]
    answer = int(fout.readline().strip())
    return n % 10 == 4 and answer == 0

problem.generate(regen_func=regen_when_zero)
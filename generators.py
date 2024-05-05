import random

def edge_generator(n: int, weight: int = None):
    """Generates a pair of integer (u, v) or triplet (u, v, w) such as 
    (1 <= u, v <= n) and (u != v) and (1 <= w <= weight).

    Uses uniform sampling for all outputs.

    Args:
        n (int): number of vertices
        weight (int, optional): maximum value of weight. Defaults to None.

    Returns:
        tuple: tuple representing the edge
    """
    while True:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v:
            break

    if weight is None:
        return (u, v)
    else:
        w = random.randint(1, weight)
        return (u, v, w)
        
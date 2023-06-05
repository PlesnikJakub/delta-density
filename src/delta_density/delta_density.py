
def max_edges(n: int) -> float:
    """Return the maximum number of nodes that could exist in
    undirected network of size n.
    """
    return n * (n - 1) / 2


def delta_density(n: int, m: int, delta: float) -> float:
    """Returns delta density for network with number of nodes n,
    number of edges m, and delta parameter.
    """
    return (aritmet(m, delta) / (aritmet(m, delta) + max_edges(n) - m))


def aritmet(m: int, delta: float) -> float:
    """Returns value of aritmetical sequence"""
    return m * (2 + delta * (1 + m)) / 2


def delta_param(n: int, k: float, d: float) -> float:
    """Returns value of delta parameter for
    number of nodes n, average degree k,
    and expected value of delta density d
    """
    return 4 * (d * n - d - k) / ((1 - d) * k * (k * n + 2))

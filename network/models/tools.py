import numpy as np


def random_choice(seq, size=2):
    """ Generate a random choice of given size with no repeating.

        Args:
            seq (list): a list of elements to choose from, elements can be repeated
            size=2 (integer): size of the random set

        Returns:
            Set of random elements of given size

        References:
            .. [1] The SciPy community,
            Numpy.random.choice,
            https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html
            .. [2] NetworkX Developers,
            NetworkX
            https://github.com/networkx/networkx/networkx/generators/random_graphs.py
    """
    targets = set()

    while len(targets) < size:
        x = np.random.choice(seq)

        targets.add(x)

    return list(targets)

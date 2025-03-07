from itertools import product
from sage.all import Compositions

def weak_compositions(n, k):
    padded_compositions = []
    for comp in Compositions(n):
        for padding in product(range(k - len(comp) + 1), repeat=len(comp) + 1):
            padded_comp = []
            for i, part in enumerate(comp):
                padded_comp.extend([0] * padding[i])
                padded_comp.append(part)
            padded_comp.extend([0] * padding[-1])
            if len(padded_comp) == k:
                padded_compositions.append(padded_comp)

    return padded_compositions
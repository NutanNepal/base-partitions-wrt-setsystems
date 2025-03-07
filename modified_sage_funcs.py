from itertools import combinations
from sage.all import matroids

def bases_iterator(M):
    for Xt in combinations(M.groundset(), M.full_rank()):
        X = frozenset(Xt)
        if M._is_independent(X):
            yield X
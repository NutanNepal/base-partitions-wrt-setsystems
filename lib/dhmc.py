import numpy as np
import itertools

def capacity(I, A, alpha):
    """
    Subroutine Capacity(I)
    I: A list or set of set indices (0-indexed).
    A: n x m binary incidence matrix (numpy array). A[i, j] = 1 if u_i in S_j.
    alpha: list/array of element multiplicities (length n).
    """
    n, m = A.shape
    neighborhood = set()
    for j in I:
        for i in range(n):
            if A[i, j] == 1:
                neighborhood.add(i)
    
    cap = sum(alpha[i] for i in neighborhood)
    return cap

def is_dhmc_valid(beta, A, alpha):
    """
    Subroutine Is_DHMC_Valid(beta)
    """
    n, m = A.shape
    # Check all non-empty subsets I of {0, ..., m-1}
    for r in range(1, m + 1):
        for I in itertools.combinations(range(m), r):
            demand = sum(beta[j] for j in I)
            cap = capacity(I, A, alpha)
            if demand > cap - 1:
                return False
    return True

def generate_compositions(k, m):
    """
    Generate all non-negative integer vectors beta of length m such that sum(beta) = k.
    This corresponds to stars and bars compositions.
    """
    if m == 1:
        yield (k,)
        return
    for i in range(k + 1):
        for tail in generate_compositions(k - i, m - 1):
            yield (i,) + tail

def dhmc_transversalization(A, alpha):
    """
    Main DHMC Transversalization function
    A: n x m binary incidence matrix.
    alpha: element multiplicities of length n.
    """
    A = np.array(A)
    n, m = A.shape
    d = sum(alpha)
    k = d - 1
    
    if k < 0:
        return []
        
    candidates = generate_compositions(k, m)
    valid_betas = []
    
    for beta in candidates:
        if is_dhmc_valid(beta, A, alpha):
            valid_betas.append(list(beta))
            
    return valid_betas

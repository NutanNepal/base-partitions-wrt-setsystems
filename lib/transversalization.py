import collections

def max_flow(n_nodes, source, sink, edges):
    """
    Computes maximum flow in a network using the Edmonds-Karp algorithm.
    edges: list of tuples (u, v, capacity)
    """
    capacity = {i: {} for i in range(n_nodes)}
    for u, v, cap in edges:
        if v not in capacity[u]:
            capacity[u][v] = 0
            capacity[v][u] = 0
        capacity[u][v] += cap

    flow = 0
    while True:
        parent = {}
        queue = collections.deque([source])
        while queue:
            curr = queue.popleft()
            if curr == sink:
                break
            for neighbor, cap in capacity[curr].items():
                if neighbor not in parent and neighbor != source and cap > 0:
                    parent[neighbor] = curr
                    queue.append(neighbor)
                    
        if sink not in parent:
            break
            
        path_flow = float('inf')
        curr = sink
        while curr != source:
            p = parent[curr]
            path_flow = min(path_flow, capacity[p][curr])
            curr = p
            
        curr = sink
        while curr != source:
            p = parent[curr]
            capacity[p][curr] -= path_flow
            capacity[curr][p] += path_flow
            curr = p
            
        flow += path_flow
        
    return flow

def weak_compositions(sum_val, num_parts):
    """Generates all weak compositions of `sum_val` into `num_parts`."""
    if num_parts == 1:
        yield (sum_val,)
        return
    for i in range(sum_val + 1):
        for tail in weak_compositions(sum_val - i, num_parts - 1):
            yield (i,) + tail

def check_admits_transversal(alpha, beta, S):
    """
    Checks if multiset alpha admits an S-transversal to composition beta.
    alpha: tuple/list of ints, len n
    beta: tuple/list of ints, len m
    S: list of m sets/lists of ints (elements range from 0 to n-1)
    """
    if sum(alpha) != sum(beta):
        return False
        
    n = len(alpha)
    m = len(beta)
    
    # An immediate fast check to reject if a set demands more elements than it contains
    for i in range(m):
        if beta[i] > len(S[i]):
            return False
            
    source = 0
    sink = n + m + 1
    edges = []
    
    # Auto-detect 1-based indexing
    all_elements = set(j for s in S for j in s)
    shift = 1 if all_elements and max(all_elements) == n else 0
    
    # Edges from Source to Left (elements)
    for j in range(n):
        if alpha[j] > 0:
            edges.append((source, j + 1, alpha[j]))
            
    # Edges from Left to Right (Set System adjacency)
    # Capacity is exactly 1 because the transversal condition requires T_i to be a subset of S_i.
    for i in range(m):
        for j in S[i]:
            idx = j - shift
            if idx >= 0 and idx < n and alpha[idx] > 0:
                edges.append((idx + 1, n + 1 + i, 1))
                
    # Edges from Right (Sets) to Sink
    for i in range(m):
        if beta[i] > 0:
            edges.append((n + 1 + i, sink, beta[i]))
            
    flow = max_flow(n + m + 2, source, sink, edges)
    return flow == sum(alpha)

def check_admits_transversal_S_beta(alpha, beta, S):
    """
    An alternative presentation where S_beta is constructed explicitly 
    by repeating S_i beta_i times. Used to check transversal matching.
    """
    if sum(alpha) != sum(beta):
        return False
        
    S_beta = []
    for i, b in enumerate(beta):
        for _ in range(b):
            S_beta.append(S[i])
            
    r = len(S_beta)
    n = len(alpha)
    source = 0
    sink = n + r + 1
    edges = []
    
    # Auto-detect 1-based indexing
    all_elements = set(j for s in S for j in s)
    shift = 1 if all_elements and max(all_elements) == n else 0
    
    for j in range(n):
        if alpha[j] > 0:
            edges.append((source, j + 1, alpha[j]))
            
    for k in range(r):
        for j in S_beta[k]:
            idx = j - shift
            if idx >= 0 and idx < n and alpha[idx] > 0:
                edges.append((idx + 1, n + 1 + k, 1))
                
    for k in range(r):
        edges.append((n + 1 + k, sink, 1))
        
    flow = max_flow(n + r + 2, source, sink, edges)
    return flow == sum(alpha)

def get_valid_betas(alpha, S):
    """
    Given a monomial exponent tuple (alpha) and a set system S,
    returns a list of all valid weak compositions (beta) such that 
    alpha admits an S-transversal to beta.
    
    alpha: tuple/list of ints, len n
    S: list of m sets/lists of ints (elements range from 0 to n-1)
    """
    valid_betas = []
    r = sum(alpha)
    m = len(S)
    
    for beta in weak_compositions(r, m):
        if check_admits_transversal(alpha, beta, S):
            valid_betas.append(tuple(beta))
            
    return valid_betas

def get_exp_gen_fn(alpha, S):
    """
    Given a monomial exponent tuple (alpha) and a set system S,
    returns the transversalized polynomial, represented as a dictionary
    mapping valid beta exponent tuples to their coefficients (which are 1.0 
    since this simply evaluates the exponential generating function of R_alpha(S)).
    
    alpha: tuple/list of ints, len n
    S: list of m sets/lists of ints (elements range from 0 to n-1)
    """
    valid_betas = get_valid_betas(alpha, S)
    
    # The transversalization operator maps x^alpha / alpha! 
    # to sum_{beta in R_alpha(S)} y^beta / beta!
    # Here we return the generated Q(y) polynomial for a single alpha.
    result = collections.defaultdict(float)
    for beta in valid_betas:
        result[beta] += 1.0
        
    return dict(result)

def transversalize_polynomial(poly, S):
    """
    Applies the transversalization operator to a full polynomial along set system S.
    poly: dict mapping tuple (alpha) to a coefficient c_alpha.
    S: list of m sets/lists over {0...n-1}
    """
    result = {}
    
    for alpha, c_alpha in poly.items():
        if c_alpha == 0:
            continue
            
        gen_fn = get_exp_gen_fn(alpha, S)
        for beta, fn_coef in gen_fn.items():
            if beta not in result:
                result[beta] = 0.0
            result[beta] += float(c_alpha) * float(fn_coef)
                
    return {beta: float(coef) for beta, coef in result.items() if coef != 0}

if __name__ == "__main__":
    # Test cases to verify the two methods match exactly
    S = [{0, 1}, {1, 2}, {0, 2}]
    alpha = (1, 1, 1) # using elements [0, 1, 2] exactly once
    beta = (1, 1, 1)  # one from each set
    
    assert check_admits_transversal(alpha, beta, S) == True
    assert check_admits_transversal_S_beta(alpha, beta, S) == True

    # Test the new functions
    valid_betas = get_valid_betas(alpha, S)
    print("Valid betas for alpha=(1,1,1):", valid_betas)
    
    gen_fn = get_exp_gen_fn(alpha, S)
    print("Exponential generating function for alpha=(1,1,1):", gen_fn)

    # Poly test
    poly = {(1, 1, 1): 1.0}
    t_poly = transversalize_polynomial(poly, S)
    print("Transversalized poly for (1, 1, 1):", t_poly)
    
    print("All checks passed.")

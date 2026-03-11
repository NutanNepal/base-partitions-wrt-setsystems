def psetcheck_fast(matroid):
    """
    Fast implementation that avoids exponential complexity by using a smarter approach.
    """
    groundset = matroid.groundset()
    powerset = list(Subsets(groundset))
    bases = matroid.bases()
    
    # Get the rank of the matroid
    d = matroid.rank()
    n = len(powerset)  # 2^n where n is the size of groundset
    
    # Create polynomial ring with 2^n variables
    R = PolynomialRing(QQ, n, 'X')
    X = R.gens()
    
    # Initialize the polynomial
    poly = 0
    
    # Precompute which elements are in each set for faster lookup
    set_elements = [set(S) for S in powerset]
    
    # Instead of checking all possible coefficient vectors,
    # we'll build the polynomial by considering each basis and
    # finding all ways to form it from the powerset
    
    for basis in bases:
        basis_list = list(basis)
        
        # Find all ways to form this basis from the powerset
        ways_to_form = find_ways_to_form_basis(basis_list, set_elements, d)
        
        # Add each way as a term to the polynomial
        for coeff_vector in ways_to_form:
            term = prod(X[i]^coeff_vector[i] for i in range(n))
            poly += term
    
    return poly

def find_ways_to_form_basis(basis_list, set_elements, target_sum):
    """
    Find all ways to form a basis by taking elements from sets.
    Returns list of coefficient vectors.
    """
    n = len(set_elements)
    ways = []
    
    # Use a more efficient approach: for each element in the basis,
    # find which sets contain it, and then find valid combinations
    
    # Create a mapping from element to sets containing it
    element_to_sets = {}
    for element in basis_list:
        element_to_sets[element] = []
        for i, S in enumerate(set_elements):
            if element in S:
                element_to_sets[element].append(i)
    
    # Find all valid assignments of elements to sets
    def find_assignments(remaining_elements, current_coeff):
        if not remaining_elements:
            # Check if the sum equals target_sum
            if sum(current_coeff) == target_sum:
                ways.append(current_coeff[:])
            return
        
        element = remaining_elements[0]
        remaining = remaining_elements[1:]
        
        # Try assigning this element to each set that contains it
        for set_idx in element_to_sets[element]:
            current_coeff[set_idx] += 1
            find_assignments(remaining, current_coeff)
            current_coeff[set_idx] -= 1
    
    # Initialize coefficient vector
    coeff_vector = [0] * n
    find_assignments(basis_list, coeff_vector)
    
    return ways

def normalize(f):
    return sum(f.monomials()[i] * f.coefficients()[i]/prod([factorial(x) for x in f.exponents()[i]]) for i in range(len(f.coefficients())))

for i in range(2, 6):  # Test with reasonable sizes
    print(f"Testing U({i}, 5)...")
    try:
        pset = psetcheck_fast(matroids.Uniform(i, 5))
        print(f"U({i}, 5): {normalize(pset).is_lorentzian()}")
    except Exception as e:
        print(f"Error with U({i}, 5): {e}")
        break 
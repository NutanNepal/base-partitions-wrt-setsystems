def psetcheck(matroid):
    groundset = matroid.groundset()
    powerset = list(Subsets(groundset))
    print(powerset)
    bases = matroid.bases()
    
    # Get the rank of the matroid
    d = matroid.rank()
    n = len(powerset)  # 2^n where n is the size of groundset
    
    # Create polynomial ring with 2^n variables
    R = PolynomialRing(QQ, n, 'X')
    X = R.gens()
    
    # Initialize the polynomial
    poly = 0
    
    # Generate all possible combinations of nonnegative integers that sum to d
    from sage.combinat.integer_vector import IntegerVectors
    
    for coeff_vector in IntegerVectors(d, n):
        # coeff_vector[i] represents how many elements to take from S_i
        count = 0
        
        # For each basis, check if we can form it by taking a_i elements from S_i
        for basis in bases:
            # Check if this basis can be formed by the current coefficient vector
            if can_form_basis_from_sets(basis, powerset, coeff_vector):
                count += 1
        
        # Add the term to the polynomial
        if count > 0:
            term = count * prod(X[i]^coeff_vector[i] for i in range(n))
            poly += term
    
    return poly

def can_form_basis_from_sets(basis, powerset, coeff_vector):
    """
    Check if a basis can be formed by taking coeff_vector[i] elements from powerset[i]
    """
    # Check if we can form the basis with the given constraints
    basis_list = list(basis)
    
    # For each set S_i, we need to take exactly coeff_vector[i] elements from it
    # We need to find a way to partition the basis elements among the sets
    
    # Try all possible ways to assign basis elements to sets
    from sage.combinat.partition import Partitions
    
    # Create a list of sets with their allowed counts
    set_assignments = []
    for i, count in enumerate(coeff_vector):
        if count > 0:
            set_assignments.append((powerset[i], count))
    
    # If no sets to assign to, basis must be empty
    if not set_assignments:
        return len(basis_list) == 0
    
    # Try all possible ways to partition the basis elements
    # This is equivalent to finding all ways to assign elements to sets
    # such that each set gets at most its allowed count
    
    def can_assign_elements_to_sets(elements, set_assignments):
        if not elements:
            return True
        
        if not set_assignments:
            return False
        
        current_set, max_count = set_assignments[0]
        remaining_sets = set_assignments[1:]
        
        # Try all possible numbers of elements to assign to current set
        for count in range(min(len(elements), max_count) + 1):
            # Check if we can assign 'count' elements from 'elements' to 'current_set'
            if count == 0:
                # Don't assign any elements to current set
                if can_assign_elements_to_sets(elements, remaining_sets):
                    return True
            else:
                # Try all possible combinations of 'count' elements
                from sage.combinat.combination import Combinations
                for selected_elements in Combinations(elements, count):
                    # Check if all selected elements are in current_set
                    if all(elem in current_set for elem in selected_elements):
                        # Remove selected elements and try to assign remaining
                        remaining_elements = [e for e in elements if e not in selected_elements]
                        if can_assign_elements_to_sets(remaining_elements, remaining_sets):
                            return True
        
        return False
    
    return can_assign_elements_to_sets(basis_list, set_assignments)

def normalize(f):
    return sum(f.monomials()[i] * f.coefficients()[i]/prod([factorial(x) for x in f.exponents()[i]]) for i in range(len(f.coefficients())))

pset = psetcheck(matroids.catalog.Fano())
print("Polynomial:")
print(pset)
print(normalize(pset).is_lorentzian())
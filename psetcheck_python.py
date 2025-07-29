import itertools
from collections import defaultdict

def powerset(iterable):
    """Generate the powerset of an iterable."""
    s = list(iterable)
    return [set(subset) for subset in itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )]

def integer_vectors(n, k):
    """Generate all integer vectors of length n that sum to k."""
    if n == 1:
        return [[k]]
    
    result = []
    for i in range(k + 1):
        for vec in integer_vectors(n - 1, k - i):
            result.append([i] + vec)
    return result

def can_form_basis_from_sets(basis, powerset_list, coeff_vector):
    """
    Check if a basis can be formed by taking coeff_vector[i] elements from powerset_list[i]
    """
    basis_list = list(basis)
    
    # Create a list of sets with their allowed counts
    set_assignments = []
    for i, count in enumerate(coeff_vector):
        if count > 0:
            set_assignments.append((powerset_list[i], count))
    
    # If no sets to assign to, basis must be empty
    if not set_assignments:
        return len(basis_list) == 0
    
    def can_assign_elements_to_sets(elements, set_assignments):
        if not elements:
            return True
        
        if not set_assignments:
            return False
        
        current_set, max_count = set_assignments[0]
        remaining_sets = set_assignments[1:]
        
        # Try all possible numbers of elements to assign to current set
        for count in range(min(len(elements), max_count) + 1):
            if count == 0:
                # Don't assign any elements to current set
                if can_assign_elements_to_sets(elements, remaining_sets):
                    return True
            else:
                # Try all possible combinations of 'count' elements
                for selected_elements in itertools.combinations(elements, count):
                    # Check if all selected elements are in current_set
                    if all(elem in current_set for elem in selected_elements):
                        # Remove selected elements and try to assign remaining
                        remaining_elements = [e for e in elements if e not in selected_elements]
                        if can_assign_elements_to_sets(remaining_elements, remaining_sets):
                            return True
        
        return False
    
    return can_assign_elements_to_sets(basis_list, set_assignments)

def psetcheck_python(groundset, bases, rank):
    """
    Pure Python implementation of the polynomial construction.
    
    Args:
        groundset: set of ground elements
        bases: list of basis sets
        rank: rank of the matroid
    """
    powerset_list = powerset(groundset)
    n = len(powerset_list)  # 2^n where n is the size of groundset
    
    # Initialize polynomial as a dictionary mapping monomial tuples to coefficients
    polynomial = defaultdict(int)
    
    # Generate all possible combinations of nonnegative integers that sum to rank
    for coeff_vector in integer_vectors(n, rank):
        count = 0
        
        # For each basis, check if we can form it by taking a_i elements from S_i
        for basis in bases:
            if can_form_basis_from_sets(basis, powerset_list, coeff_vector):
                count += 1
        
        # Add the term to the polynomial
        if count > 0:
            # Convert coefficient vector to monomial tuple
            monomial = tuple(coeff_vector)
            polynomial[monomial] += count
    
    return polynomial

def format_polynomial(poly_dict, var_names=None):
    """Format the polynomial dictionary as a readable string."""
    if not poly_dict:
        return "0"
    
    terms = []
    for monomial, coeff in sorted(poly_dict.items()):
        if coeff == 0:
            continue
        
        # Build the term
        term_parts = []
        if coeff != 1:
            term_parts.append(str(coeff))
        
        for i, power in enumerate(monomial):
            if power > 0:
                var_name = var_names[i] if var_names else f"X{i}"
                if power == 1:
                    term_parts.append(var_name)
                else:
                    term_parts.append(f"{var_name}^{power}")
        
        if not term_parts:
            term_parts.append("1")
        
        terms.append("*".join(term_parts))
    
    return " + ".join(terms)

# Example usage
if __name__ == "__main__":
    # Example: U(2,2) matroid
    groundset = frozenset({'f', 'g', 'c', 'b', 'a', 'e', 'd'})
    bases = [frozenset({'a', 'c', 'b'}), frozenset({'a', 'c', 'd'}), frozenset({'a', 'b', 'd'}), frozenset({'a', 'e', 'd'}), frozenset({'e', 'b', 'd'}), frozenset({'c', 'e', 'd'}), frozenset({'c', 'e', 'b'}), frozenset({'a', 'e', 'b'}), frozenset({'a', 'e', 'f'}), frozenset({'e', 'b', 'f'}), frozenset({'c', 'e', 'f'}), frozenset({'a', 'f', 'd'}), frozenset({'b', 'f', 'd'}), frozenset({'c', 'f', 'd'}), frozenset({'a', 'c', 'f'}), frozenset({'c', 'b', 'f'}), frozenset({'a', 'g', 'f'}), frozenset({'g', 'b', 'f'}), frozenset({'g', 'f', 'd'}), frozenset({'g', 'e', 'f'}), frozenset({'a', 'e', 'g'}), frozenset({'g', 'c', 'e'}), frozenset({'g', 'e', 'd'}), frozenset({'g', 'b', 'd'}), frozenset({'g', 'c', 'd'}), frozenset({'a', 'c', 'g'}), frozenset({'g', 'c', 'b'}), frozenset({'a', 'g', 'b'})]
    rank = 3
    
    print("Groundset:", groundset)
    print("Bases:", bases)
    print("Rank:", rank)
    print()
    
    poly = psetcheck_python(groundset, bases, rank)
    print("Polynomial (dictionary form):")
    print(poly)
    print()
    
    print("Polynomial (formatted):")
    print(format_polynomial(poly)) 
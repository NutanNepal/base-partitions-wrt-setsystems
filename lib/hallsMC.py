def check_halls_marriage_condition(set_system):
    """
    Checks if a family of subsets satisfies Hall's Marriage Condition.
    
    Hall's Marriage Condition states that for any subcollection of sets,
    the size of their union is at least as large as the number of sets in the subcollection.
    This is equivalent to the existence of a system of distinct representatives (SDR).
    We can efficiently solve this by computing a maximum bipartite matching.
    
    Args:
        set_system: An iterable of iterables (e.g., list of lists or list of sets), 
                    where each sub-iterable represents a set in the system.
        
    Returns:
        bool: True if Hall's condition is satisfied, False otherwise.
    """
    # Convert input to a list of iterables to allow repeatable iteration
    subsets = [list(s) for s in set_system]
    
    # Optimization: if the total number of unique elements is less than the number 
    # of subsets, the condition is immediately violated for the full collection.
    total_elements = set()
    for s in subsets:
        total_elements.update(s)
        
    if len(total_elements) < len(subsets):
        return False
        
    match = {} # Maps element -> index of the subset it represents
    
    # DFS to find an augmenting path
    def dfs(u, visited):
        for v in subsets[u]:
            if v not in visited:
                visited.add(v)
                # If element v is not matched, or its current match can be assigned elsewhere
                if v not in match or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    # Try to find a representative for each subset
    for i in range(len(subsets)):
        if not dfs(i, set()):
            return False # Could not find a distinct representative for subset i
            
    return True

if __name__ == "__main__":
    # Simple test cases
    assert check_halls_marriage_condition([{1, 3}, {1, 3}, {1, 3}]) == True
    assert check_halls_marriage_condition([{1, 2}, {1, 2}, {1, 2}]) == False
    assert check_halls_marriage_condition([{1}, {2}, {3}]) == True
    print("All tests passed.")

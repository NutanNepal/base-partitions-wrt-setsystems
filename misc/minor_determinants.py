import numpy as np

def get_minor_determinant_matrix(M):
    """
    Compute matrix H where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}
    
    Args:
        M: Input matrix (n x n)
    
    Returns:
        Matrix H of size n x n where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}
    """
    n, m = M.shape
    
    if n != m:
        raise ValueError("Matrix must be square")
    
    # Initialize result matrix
    H = np.zeros((n, n))
    
    # Compute each entry h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}
    for i in range(n):
        for j in range(n):
            H[i, j] = M[i, i] * M[j, j] - M[i, j] * M[j, i]
    
    return H

# Example usage with a 4x4 matrix
M = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Original Matrix M:")
print(M)
print()

# Compute matrix H where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}
H = get_minor_determinant_matrix(M)

print("Matrix H where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}:")
print(H)
print()

print("Matrix properties:")
print(f"Shape: {H.shape}")
print(f"Is symmetric: {np.allclose(H, H.T)}")
print(f"Determinant: {np.linalg.det(H):.6f}")
print(f"Trace: {np.trace(H):.6f}")
print(f"All entries >= 0: {np.all(H >= 0)}")

# Let's also try with a symmetric matrix
print("\n" + "="*50)
print("Example with symmetric matrix:")

M_sym = np.array([
    [3, 1, 0, 2],
    [1, 4, 2, 0],
    [0, 2, 5, 1],
    [2, 0, 1, 3]
])

print("Original symmetric matrix M:")
print(M_sym)
print()

H_sym = get_minor_determinant_matrix(M_sym)
print("Matrix H for symmetric M:")
print(H_sym)
print()

print("Properties of H for symmetric M:")
print(f"Is symmetric: {np.allclose(H_sym, H_sym.T)}")
print(f"Determinant: {np.linalg.det(H_sym):.6f}")
print(f"Trace: {np.trace(H_sym):.6f}")
print(f"All entries >= 0: {np.all(H_sym >= 0)}") 
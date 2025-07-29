import numpy as np

def get_P_matrix(M):
    """
    Compute matrix P where P_{ij} = m_{ii} * m_{jj}
    
    Args:
        M: Input matrix (n x n)
    
    Returns:
        Matrix P of size n x n where P_{ij} = m_{ii} * m_{jj}
    """
    n, m = M.shape
    
    if n != m:
        raise ValueError("Matrix must be square")
    
    # Initialize result matrix with integer dtype
    P = np.zeros((n, n), dtype=int)
    
    # Compute each entry P_{ij} = m_{ii} * m_{jj}
    for i in range(n):
        for j in range(n):
            P[i, j] = M[i, i] * M[j, j]
    
    return P

# Example usage with the same 5x5 matrix
M = np.array([
    [3, 1, 0, 2, 1],
    [1, 4, 2, 0, 1],
    [0, 2, 5, 1, 0],
    [2, 0, 1, 3, 2],
    [1, 1, 0, 2, 4]
])

print("Original Matrix M:")
print(M)
print()

P = get_P_matrix(M)
print("Matrix P where P_{ij} = m_{ii} * m_{jj}:")
print(P)
print()

print("Matrix properties:")
print(f"Shape: {P.shape}")
print(f"Is symmetric: {np.allclose(P, P.T)}")
print(f"Determinant: {np.linalg.det(P)}")
print(f"Trace: {np.trace(P)}")
print(f"All entries >= 0: {np.all(P >= 0)}")
print(f"Data type: {P.dtype}")
print(f"All entries are integers: {np.all(P == P.astype(int))}")

# Show the diagonal entries of M for verification
print(f"\nDiagonal entries of M: {np.diag(M)}")
print("Verification of P entries:")
for i in range(5):
    for j in range(5):
        expected = M[i,i] * M[j,j]
        actual = P[i,j]
        print(f"P[{i},{j}] = {M[i,i]} * {M[j,j]} = {expected} ✓")

# Compare with H matrix
def get_H_matrix(M):
    """Compute matrix H where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}"""
    n = M.shape[0]
    H = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            H[i,j] = M[i,i] * M[j,j] - M[i,j] * M[j,i]
    return H

H = get_H_matrix(M)
print(f"\nMatrix H (for comparison):")
print(H)
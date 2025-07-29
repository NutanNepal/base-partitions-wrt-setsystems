import numpy as np

M = np.array([
    [3, 1, 0, 2, 1],
    [1, 4, 2, 0, 1],
    [0, 2, 5, 1, 0],
    [2, 0, 1, 3, 2],
    [1, 1, 0, 2, 4]
])

def get_minor_determinant_matrix(M):
    """
    Compute matrix H where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}
    
    Args:
        M: Input matrix (n x n)
    
    Returns:
        Matrix H of size n x n where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}
        All entries are integers.
    """
    n, m = M.shape
    
    if n != m:
        raise ValueError("Matrix must be square")
    
    # Initialize result matrix with integer dtype
    H = np.zeros((n, n), dtype=int)
    
    # Compute each entry h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}
    for i in range(n):
        for j in range(n):
            H[i, j] = int(M[i, i] * M[j, j] - M[i, j] * M[j, i])
    
    return H
    
print("Original Matrix M:")
print(M)
print()

H = get_minor_determinant_matrix(M)
print("Matrix H where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}:")
print(H)
print()

print("Matrix properties:")
print(f"Shape: {H.shape}")
print(f"Is symmetric: {np.allclose(H, H.T)}")
print(f"Determinant: {np.linalg.det(H)}")
print(f"Trace: {np.trace(H)}")
print(f"All entries >= 0: {np.all(H >= 0)}")
print(f"Data type: {H.dtype}")
print(f"All entries are integers: {np.all(H == H.astype(int))}") 
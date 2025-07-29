import numpy as np

# Create a 5x5 symmetric matrix with positive diagonal and non-negative off-diagonal entries
matrix = np.array([
    [3, 1, 0, 2, 1],
    [1, 4, 2, 0, 1],
    [0, 2, 5, 1, 0],
    [2, 0, 1, 3, 2],
    [1, 1, 0, 2, 4]
])

print("5x5 Symmetric Matrix:")
print(matrix)
print()
print("Matrix properties:")
print(f"Shape: {matrix.shape}")
print(f"Is symmetric: {np.allclose(matrix, matrix.T)}")
print(f"Diagonal entries (all positive): {np.diag(matrix)}")
print(f"Off-diagonal entries (all non-negative): {matrix[np.triu_indices(5, k=1)]}")
print(f"All entries >= 0: {np.all(matrix >= 0)}")
print(f"All diagonal entries > 0: {np.all(np.diag(matrix) > 0)}") 
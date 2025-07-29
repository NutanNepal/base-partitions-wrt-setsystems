# SageMath script for computing eigenvalues
# Run this in SageMath environment

# Define a matrix
M = matrix([
    [3, 1, 0, 2, 1],
    [1, 4, 2, 0, 1],
    [0, 2, 5, 1, 0],
    [2, 0, 1, 3, 2],
    [1, 1, 0, 2, 4]
])

print("Original Matrix M:")
print(M)
print()

# Method 1: Compute all eigenvalues
eigenvalues = M.eigenvalues()
print("Eigenvalues of M:")
print(eigenvalues)
print()

# Method 2: Compute eigenvalues with multiplicities
eigenvalues_with_multiplicities = M.eigenvalues()
print("Eigenvalues with multiplicities:")
for ev in eigenvalues_with_multiplicities:
    print(f"λ = {ev}")
print()

# Method 3: Compute characteristic polynomial
char_poly = M.characteristic_polynomial()
print("Characteristic polynomial:")
print(char_poly)
print()

# Method 4: Compute eigenvalues and eigenvectors
eigenpairs = M.eigenmatrix_right()
eigenvalues_eigenpairs = eigenpairs[0]
eigenvectors = eigenpairs[1]

print("Eigenvalues from eigenmatrix:")
print(eigenvalues_eigenpairs)
print()

print("Eigenvectors matrix:")
print(eigenvectors)
print()

# Method 5: Check if matrix is positive definite
is_positive_definite = all(ev > 0 for ev in eigenvalues)
print(f"Is positive definite: {is_positive_definite}")

# Method 6: Check if matrix is positive semidefinite
is_positive_semidefinite = all(ev >= 0 for ev in eigenvalues)
print(f"Is positive semidefinite: {is_positive_semidefinite}")

# Method 7: Compute singular values (for comparison)
singular_values = M.singular_values()
print(f"Singular values: {singular_values}")

# Method 8: Compute the H matrix and check its eigenvalues
def get_minor_determinant_matrix(M):
    """Compute matrix H where h_{ij} = m_{ii} * m_{jj} - m_{ij} * m_{ji}"""
    n = M.nrows()
    H = matrix(n, n)
    for i in range(n):
        for j in range(n):
            H[i,j] = M[i,i] * M[j,j] - M[i,j] * M[j,i]
    return H

H = get_minor_determinant_matrix(M)
print("\nMatrix H:")
print(H)
print()

H_eigenvalues = H.eigenvalues()
print("Eigenvalues of H:")
print(H_eigenvalues)
print()

# Check properties of H eigenvalues
H_is_positive_semidefinite = all(ev >= 0 for ev in H_eigenvalues)
print(f"Is H positive semidefinite: {H_is_positive_semidefinite}")

# Method 9: Compute eigenvalues numerically (for large matrices)
eigenvalues_numeric = M.eigenvalues(algorithm='numpy')
print(f"\nEigenvalues (numerical): {eigenvalues_numeric}")

# Method 10: Check spectral radius
spectral_radius = max(abs(ev) for ev in eigenvalues)
print(f"Spectral radius: {spectral_radius}") 


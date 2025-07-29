# Simple SageMath script for eigenvalues
# Save as .sage file and run in SageMath

# Import combinations from SageMath
from sage.combinat.combination import Combinations

# Define your matrix
M = matrix([
    [0, 1, 1, 1, 1, 2, 2],
    [1, 0, 1, 1, 2, 1, 2],
    [1, 1, 0, 2, 1, 1, 2],
    [1, 1, 2, 1, 2, 3, 3],
    [1, 2, 1, 2, 1, 3, 3],
    [2, 1, 1, 3, 3, 1, 3],
    [2, 2, 2, 3, 3, 3, 3],
])

print("Matrix M:")
print(M)
print()

# Basic eigenvalue computation
eigenvalues = M.eigenvalues()
print("Eigenvalues:")
print(eigenvalues)
print()

# Check if positive definite/semidefinite
is_positive_definite = all(ev > 0 for ev in eigenvalues)
is_positive_semidefinite = all(ev >= 0 for ev in eigenvalues)

print(f"Positive definite: {is_positive_definite}")
print(f"Positive semidefinite: {is_positive_semidefinite}")
print()

# Compute H matrix and its eigenvalues
def H_matrix(M):
    n = M.nrows()
    H = matrix(n, n)
    for i in range(n):
        for j in range(n):
            H[i,j] = M[i,i] * M[j,j] - M[i,j] * M[j,i]
    return H

H = H_matrix(M)
print("Matrix H:")
print(H)
print()

H_eigenvalues = H.eigenvalues()
print("Eigenvalues of H:")
print(H_eigenvalues)
print()

H_is_positive_semidefinite = all(ev >= 0 for ev in H_eigenvalues)
print(f"Is H positive semidefinite: {H_is_positive_semidefinite}")

# L_matrix function where L_{ij} = (m_{ij} choose 2)
def L_matrix(M):
    n = M.nrows()
    L = matrix(n, n)
    for i in range(n):
        for j in range(n):
            # Compute binomial coefficient (m_{ij} choose 2)
            m_ij = M[i,j]
            if m_ij >= 2:
                L[i,j] = binomial(m_ij, 2)
            else:
                L[i,j] = 0  # (k choose 2) = 0 for k < 2
    return L

L = L_matrix(M)
print("\nMatrix L where L_{ij} = (m_{ij} choose 2):")
print(L)
print()

L_eigenvalues = L.eigenvalues()
print("Eigenvalues of L:")
print(L_eigenvalues)
print()

L_is_positive_semidefinite = all(ev >= 0 for ev in L_eigenvalues)
print(f"Is L positive semidefinite: {L_is_positive_semidefinite}")

# Compute sum of H and L matrices
H_plus_L = H + L
print("\n" + "="*50)
print("Matrix H + L:")
print(H_plus_L)
print()

# Compute eigenvalues of H + L
H_plus_L_eigenvalues = H_plus_L.eigenvalues()
print("Eigenvalues of H + L:")
print(H_plus_L_eigenvalues)
print()

H_plus_L_is_positive_semidefinite = all(ev >= 0 for ev in H_plus_L_eigenvalues)
print(f"Is H + L positive semidefinite: {H_plus_L_is_positive_semidefinite}")

# Summary of all matrices
print("\n" + "="*50)
print("SUMMARY:")
print(f"Matrix M - Positive semidefinite: {is_positive_semidefinite}")
print(f"Matrix H - Positive semidefinite: {H_is_positive_semidefinite}")
print(f"Matrix L - Positive semidefinite: {L_is_positive_semidefinite}")
print(f"Matrix H + L - Positive semidefinite: {H_plus_L_is_positive_semidefinite}")
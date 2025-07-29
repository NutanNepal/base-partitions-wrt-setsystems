# Mathematical Definitions

## Matroid Theory

### Matroid
A **matroid** is a pair (E, ℐ) where E is a finite set (called the **ground set**) and ℐ is a collection of subsets of E (called **independent sets**) satisfying:
1. **Hereditary property**: If I ∈ ℐ and J ⊆ I, then J ∈ ℐ
2. **Exchange property**: If I, J ∈ ℐ with |I| < |J|, then there exists x ∈ J \ I such that I ∪ {x} ∈ ℐ

### Rank Function
The **rank function** r: 2^E → ℕ is defined by:
r(A) = max{|I| : I ⊆ A, I ∈ ℐ}

### Rank of a Matroid
The **rank** of a matroid M is r(E), denoted rank(M).

### Basis
A **basis** of a matroid is a maximal independent set. All bases have the same cardinality, equal to the rank of the matroid.

### Uniform Matroid
A **uniform matroid** U(r,n) is a matroid on n elements where every subset of size ≤ r is independent.

## Set Systems

### Set System
A **set system** is a collection S = (S₁, S₂, ..., Sₖ) of subsets of a ground set E.

### Decomposition of a Set System
Given a set system S = (S₁, S₂, ..., Sₖ), its **decomposition** is:
decompose(S) = ({x} : x ∈ Sᵢ for some i)

## Compositions and Partitions

### Weak Composition
A **weak composition** of n into k parts is a k-tuple (a₁, a₂, ..., aₖ) of non-negative integers such that a₁ + a₂ + ... + aₖ = n.

### Partition of a Basis
Given a basis B and a weak composition w = (w₁, w₂, ..., wₖ), a **partition** of B according to w is a k-tuple (P₁, P₂, ..., Pₖ) where:
- Pᵢ ⊆ B for all i
- |Pᵢ| = wᵢ for all i
- Pᵢ ∩ Pⱼ = ∅ for i ≠ j
- ∪ᵢ Pᵢ = B

## Polynomial Constructions

### Weighted Polynomial
Given a matroid M and set system S = (S₁, S₂, ..., Sₖ), the **weighted polynomial** is:
P(x₁, x₂, ..., xₖ) = Σᵢ wᵢ · x₁^a₁ x₂^a₂ ... xₖ^aₖ

where:
- The sum is over all weak compositions (a₁, a₂, ..., aₖ) of rank(M)
- wᵢ is the weight of composition i
- xᵢ are indeterminates

### Composition Weight
The **weight** of a composition (a₁, a₂, ..., aₖ) is the number of bases B such that there exists a partition (P₁, P₂, ..., Pₖ) of B where:
|Pᵢ ∩ Sⱼ| = aⱼ for all i, j

## Matrix Constructions

### Coefficient Matrix A(S)
For a rank 2 matroid M and set system S = (S₁, S₂, ..., Sₖ), the **coefficient matrix** A(S) is a k×k symmetric matrix where:
- A[i,i] = number of bases B such that B ⊆ Sᵢ
- A[i,j] = number of bases B = {b₁, b₂} such that (b₁ ∈ Sᵢ and b₂ ∈ Sⱼ) or (b₁ ∈ Sⱼ and b₂ ∈ Sᵢ)

## Lorentzian Polynomials

### Lorentzian Polynomial
A homogeneous polynomial f ∈ ℝ[x₁, x₂, ..., xₙ] is **Lorentzian** if:
1. All coefficients are non-negative
2. The polynomial is log-concave on the positive orthant
3. The Hessian matrix has at most one positive eigenvalue at any point in the positive orthant

### Normalization
The **normalized polynomial** of f is:
f_norm = Σᵢ (cᵢ / Πⱼ aⱼ!) · x₁^a₁ x₂^a₂ ... xₙ^aₙ

where cᵢ are the coefficients and (a₁, a₂, ..., aₙ) are the exponents.

## Special Functions

### Weak Compositions Function
```python
def weak_compositions(n, k):
    """Generate all weak compositions of n into k parts."""
```

### Bases Iterator
```python
def bases_iterator(M):
    """Iterate through all bases of matroid M."""
```

### Partition Function
```python
def partitions(basis, weak_comp):
    """Partition a basis according to a weak composition."""
```

### Weighted Polynomial Function
```python
def weighted_poly(M, set_system):
    """Compute the weighted polynomial for matroid M and set system."""
```

### Coefficient Matrix Function
```python
def get_A_matrix(S, bases):
    """Compute the coefficient matrix A(S) for rank 2 matroids."""
```

## Mathematical Properties

### Symmetric Matrix
A matrix A is **symmetric** if A = A^T.

### Positive Definite Matrix
A symmetric matrix A is **positive definite** if x^T A x > 0 for all non-zero vectors x.

### Log-Concave Function
A function f: ℝ^n → ℝ is **log-concave** if log(f) is concave, i.e., for all x, y and λ ∈ [0,1]:
f(λx + (1-λ)y) ≥ f(x)^λ f(y)^(1-λ)

## Notation

- M: Matroid
- E: Ground set
- ℐ: Collection of independent sets
- r: Rank function
- B: Basis
- S: Set system
- P: Polynomial
- A: Matrix
- w: Weight
- x: Indeterminate/variable
- λ: Parameter (usually in [0,1])
- ℝ: Real numbers
- ℕ: Natural numbers (including 0)
- ⊆: Subset
- ∩: Intersection
- ∪: Union
- ∅: Empty set
- |A|: Cardinality of set A
- A^T: Transpose of matrix A 
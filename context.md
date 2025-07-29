# Base Partitions with Respect to Set Systems

## Project Overview

This project implements computational tools for studying matroid theory, specifically focusing on base partitions with respect to set systems and their associated polynomials. The research appears to be related to Lorentzian polynomials and their properties in the context of matroid theory.

## Mathematical Background

### Core Concepts

1. **Matroids**: A matroid is a mathematical structure that generalizes the notion of linear independence. The project works with uniform matroids of rank 2.

2. **Base Partitions**: The project computes partitions of matroid bases with respect to weak compositions, where each basis is partitioned according to a composition of the matroid's rank.

3. **Set Systems**: A set system is a collection of subsets of the ground set. The project studies how bases interact with these set systems.

4. **Weighted Polynomials**: The main focus is on computing weighted polynomials that encode information about how bases partition with respect to set systems.

5. **Lorentzian Polynomials**: The project investigates whether certain polynomials are Lorentzian, which is related to log-concavity and has applications in combinatorics and optimization.

## Project Structure

### Core Files

- **`imp_funcs.py`**: Contains utility functions for generating weak compositions
- **`modified_sage_funcs.py`**: Provides a bases iterator for matroids
- **`np-n-weights.ipynb`**: Main implementation of weighted polynomial computation
- **`np-n-weights copy.ipynb`**: Extended version with additional functionality
- **`rank2case.ipynb`**: Specialized implementation for rank 2 matroids with matrix computations
- **`weights-on-all-set-systems.ipynb`**: Generates all set systems of a given size

### Key Functions

#### `weak_compositions(n, k)`
Generates all weak compositions of n into k parts using Sage's Compositions.

#### `bases_iterator(M)`
Iterates through all bases of a matroid M.

#### `partitions(basis, weak_comp)`
Partitions a basis according to a weak composition, considering all permutations.

#### `base_partitions(bases, indexed_compositions)`
Computes partitions for all bases with respect to all weak compositions.

#### `composition_weight(iwc, set_system, bp)`
Computes the weight of each composition based on intersection properties.

#### `weighted_poly(M, set_system)`
The main function that computes the weighted polynomial for a matroid and set system.

#### `get_A_matrix(S, bases)`
For rank 2 matroids, computes the coefficient matrix A(S) that encodes information about how bases interact with the set system S.

## Mathematical Framework

### Weighted Polynomial Construction

1. **Input**: A matroid M and a set system S = (S₁, ..., Sₖ)
2. **Bases**: Enumerate all bases of the matroid
3. **Compositions**: Generate all weak compositions of the matroid's rank into k parts
4. **Partitions**: For each basis and composition, partition the basis according to the composition
5. **Weights**: Compute weights based on intersection properties between partitions and set system elements
6. **Polynomial**: Construct a polynomial where each monomial corresponds to a composition, weighted by the computed weights

### Special Case: Rank 2 Matroids

For rank 2 matroids, the project implements a matrix-based approach:
- Constructs an n×n symmetric matrix A(S) where n = |S|
- A[i,i] counts bases contained in Sᵢ
- A[i,j] counts bases with one element in Sᵢ and one in Sⱼ

### Lorentzian Property

The project tests whether normalized weighted polynomials are Lorentzian, which involves:
- Normalizing polynomials by dividing coefficients by appropriate factorials
- Checking log-concavity properties
- Studying the relationship between different polynomial constructions

## Research Context

The project appears to be investigating:
1. Properties of weighted polynomials arising from matroid base partitions
2. Lorentzian properties of these polynomials
3. Relationships between different polynomial constructions (e.g., original vs. decomposed set systems)
4. Matrix representations for special cases

## Dependencies

- **SageMath**: For matroid operations and polynomial rings
- **NumPy**: For matrix computations
- **itertools**: For combinatorial operations

## References

The project includes several PDF references:
- `bh-lorentzianpolys.pdf`: Likely covers Lorentzian polynomial theory
- `Eur_LogConcRainbows.pdf`: Possibly related to log-concavity
- `anari-gharan-generalization-of-permanent-inequalities.pdf`: May cover related inequalities

## Usage

The main workflow involves:
1. Defining a matroid (typically uniform rank 2)
2. Specifying a set system
3. Computing the weighted polynomial
4. Analyzing properties like Lorentzian behavior
5. Comparing different constructions (e.g., original vs. decomposed set systems)

This project provides computational tools for studying advanced topics in matroid theory and polynomial combinatorics, with particular focus on Lorentzian polynomials and their applications. 
# DHMC Transversalization

**Inputs:**
* `A`: An $n \times m$ binary incidence matrix where $A_{i,j} = 1$ if $u_i \in S_j$.
* `alpha`: An integer vector of length $n$ representing element multiplicities.

**Outputs:**
* `Valid_Betas`: A list of integer vectors of length $m$ satisfying DHMC.

### Algorithm

**Step 1: Initialization**
1. Let $d = \sum_{i=1}^n \alpha_i$.
2. Let the target degree $k = d - 1$.
3. If $k < 0$, return an empty list (system is infeasible).

**Step 2: Define the Capacity Function**
Define a subroutine `Capacity(I)` that takes a subset of set indices $I \subseteq \{1, \dots, m\}$:
1. Initialize an empty set of elements `Neighborhood`.
2. For each set index $j \in I$:
3.   For each element index $i \in \{1, \dots, n\}$:
4.     If $A_{i,j} == 1$, add $i$ to `Neighborhood`.
5. Return the sum of $\alpha_i$ for all $i \in \text{Neighborhood}$.

**Step 3: Define the DHMC Validator**
Define a subroutine `Is_DHMC_Valid(beta)` that takes an integer vector $\beta$ of length $m$:
1. For every non-empty subset $I \subseteq \{1, \dots, m\}$:
2.   Let `demand` $= \sum_{j \in I} \beta_j$.
3.   Let `capacity` $= \text{Capacity}(I)$.
4.   If `demand` $> \text{capacity} - 1$:
5.     Return `False`.
6. Return `True`.

**Step 4: Generate and Filter Compositions**
1. Generate `Candidates`: the set of all non-negative integer vectors $\beta$ of length $m$ such that $\sum_{j=1}^m \beta_j = k$. *(Use standard stars-and-bars combinatorial generation/backtracking).*
2. Initialize an empty list `Valid_Betas`.
3. For each `beta` in `Candidates`:
4.   If `Is_DHMC_Valid(beta)` is `True`:
5.     Append `beta` to `Valid_Betas`.
6. Return `Valid_Betas`.
\begin{Obs}~\label{obs: 2-H}
    Let $S=(S_1,\ldots,S_n)$ with $\abs{S_i}=a_i$ and $\abs{S_i\cap S_j}=a_{ij}.$ Then the Hessian $H=(H_{ij})$ has entries
    $$H_{ij}=K_{ij}+L_{ij}=
        \underbrace{a_ia_j-a_{ij}^2}_{K_{ij}}+\underbrace{{a_{ij}\choose 2}}_{L_{ij}}=\underbrace{a_ia_j}_{P}-\frac{1}{2}\underbrace{(a_{ij}^2-a_{ij})}_{Q}$$
        where if $i=j$ the $H_{ij}={a_i\choose 2}.$
\end{Obs}

\begin{Th}
    $M$ is symmetric with nonnegative entries, then $M$ has one positive eigenvalue iff there exists $e\in \RR^n$ s.t. $e^TAe>0$ and for all $x\in \RR^n$ $$(e^T Ax)^2\geq (e^TAe)(x^T Ax).$$
\end{Th}
\begin{Ex}
    Consider $M= diag(1,0). $ Then we want to find $e$ s.t. the two above conditions hold. $x=(x_1,x_2)$, then $e^TAx=e^T(x_1,0)=e_1x_1.$ So $(e^T Ax)^2=(e_1x_1)^2.$ Then $e^TAe=e_1^2$ and $x^TA x=x_1^2.$ Now we want $e$ such that 
    $$e_1^2 x_1^2-(e_1x_1)^2\leq 0. $$
    Any $e$ w.t. $e_1>0$ works. 
\end{Ex}
We want to do something like this, but let's replace $M$ with $H$ and find such an $e.$
\begin{Ex}[$2\times 2$ case of idea]
    $H$ is $2\times 2$, i.p.,
    $$H=\begin{pmatrix}
        {a_{1}\choose 2} & a_1a_2-a_{12}^2+{a_{12}\choose 2}\\
        a_1a_2-a_{12}^2+{a_{12}\choose 2} & {a_{2}\choose 2}
    \end{pmatrix}.$$
\end{Ex}
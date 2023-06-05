# Δ Density

Δ Density is a new measure that considers both the density and
the average degree in such a way that allows the values of this measure to be
comparable for networks of different sizes.

The concept of ∆ density is based on the assumption that each existing edge
has a greater influence on the determination of ∆ density than a missing edge
between a pair of nodes.

## Definition
The ∆-density for a network with n nodes and m edges is defined as:

$$ ∆(δ, n, m) =  {A(m, δ) \over (A(m, δ) + M(n) − m)}$$

If we modify the formula for calculating the ∆-density we can define a δ
function. Calculation of the δ based on the network size n, average degree kavg
and the expected value of ∆-density ∆exp is as follows:

$$
δ(n, kavg, ∆exp) = {4 ∗ (d ∗ n − d − kavg) \over
((1 − d) ∗ kavg ∗ (kavg ∗ n + 2))}.
$$


## Publications

* Plesnik, J., Kubikova, K., Kudelka, M. (2023). Delta Density: Comparison of Different Sized Networks Irrespective of Their Size. In: Cherifi, H., Mantegna, R.N., Rocha, L.M., Cherifi, C., Micciche, S. (eds) Complex Networks and Their Applications XI. COMPLEX NETWORKS 2016 2022. Studies in Computational Intelligence, vol 1078. Springer, Cham. https://doi.org/10.1007/978-3-031-21131-7_29

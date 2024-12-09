# have a look at the docu examples from sympy
from sympy import flatten, symbols, unflatten
from sympy.combinatorics import PermutationGroup, Permutation, Polyhedron


# there is a great deal of documentation in the class PermutationGroup. Let's start from here

def layout():
    """
               _______
               | 1  2|
               | 3  4|
               =======
               | 5  6|
               | 7  8|
         ===================
         |17 18| 9 10|21 22|
         |19 20|11 12|23 24|
         ===================
               |13 14|
               |15 16|
               -------

               B
               T
             L F R
               D
    """
    F = Permutation(9, 11, 12, 10)(7, 20, 14, 21)(8, 18, 13, 23)
    T = Permutation(5, 7, 8, 6)(4, 17, 9, 21)(3, 18, 10, 22)
    D = Permutation(13, 15, 16, 14)(11, 19, 2, 23)(12, 20, 1, 24)
    B = Permutation(1, 3, 4, 2)(17, 6, 24, 15)(19, 5, 22, 16)
    L = Permutation(17, 19, 20, 18)(9, 5, 1, 13)(11, 7, 3, 15)
    R = Permutation(21, 23, 24, 22)(10, 14, 2, 6)(12, 16, 4, 8)
    group = PermutationGroup(F, T, D, B, L, R)
    print(group.order())
    print(3 ** 7 * 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8)

    group2 = PermutationGroup(F, R, D)
    print(group2.order())
    print(group.order() / group2.order())

def show():
    pairs = unflatten(r2.corners, 2)
    print(pairs[::2])
    print(pairs[1::2])

def facelets():
    a = Permutation(2, 1)
    b = Permutation(1, 0)
    G = PermutationGroup(a, b)
    print(G.order())

    P = Polyhedron(list('ABC'), pgroup=G)
    print(P.corners)
    P.rotate(0)
    print(P.corners)
    P.reset()
    print(P.corners)

    facelets = flatten([symbols(s + '1:5') for s in 'UFRBLD'])
    print(facelets)

def coset_factors():
    a = Permutation(0, 1, 3, 7, 6, 4)(2, 5)
    b = Permutation(0, 1, 3, 2)(4, 5, 7, 6)
    G = PermutationGroup([a, b])

    g = Permutation(7)(1, 2, 4)(3, 6, 5)

    print(G.contains(g))
    f = G.coset_factor(g)
    print("Coset factors for g")
    print(f)

    print("Show equivalence")
    print(f[2] * f[1] * f[0])
    print(g)

    f1 = G.coset_factor(g, True)
    print(f1)

    tr = G.basic_transversals
    print(f[0] == tr[0][f1[0]])

    c = Permutation(5, 6, 7)
    G.coset_factor(c)

if __name__ == '__main__':

    # layout()
    coset_factors()
    # facelets()

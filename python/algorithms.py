from sympy.combinatorics import Permutation, PermutationGroup


def learn():
    a = Permutation(1,2,3)
    b = Permutation(1,2)(3,4)
    G = PermutationGroup(a,b)
    print("Group: ",G)
    print("Order: ",G.order())
    print("Stabilizer of 1: ",G.stabilizer(1))
    print("Stabilizer of 4: ",G.stabilizer(4))
    print("Strong generators: ",G.strong_gens)
    print("Elements: ",G.elements)

if __name__ == '__main__':
    learn()
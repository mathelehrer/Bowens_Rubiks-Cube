from sympy import prod
from sympy.combinatorics import PermutationGroup, Permutation


def s3():
    group  = PermutationGroup(Permutation(1,2),Permutation(1,2,3))
    print("Order: ",group.order())
    print("Basic transversals: ",group.basic_transversals)

def d4():
    """
    dihedral group of order 4
    :return:
    """
    group = PermutationGroup(Permutation(1, 2,3,4), Permutation(1, 2)(4, 3))
    print("Order: ", group.order())
    print("Basic transversals: ", group.basic_transversals)


def s4():
    """
    dihedral group of order 4
    :return:
    """
    group = PermutationGroup(Permutation(1, 2,3,4), Permutation(1, 2))
    print("Order: ", group.order())
    print("Basic transversals: ", group.basic_transversals)

def dissect_group_order(group):
    tranversals = group.basic_transversals
    print("Transverals: ",tranversals)
    m = prod([len(x) for x in group.basic_transversals])
    return m

if __name__ == '__main__':
    # s3()
    # d4()
    print(dissect_group_order(group=PermutationGroup(Permutation(1,2,3,4))))

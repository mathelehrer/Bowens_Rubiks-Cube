from sympy.combinatorics import Permutation, PermutationGroup

# Define basic generators for the 2x2x2 cube group (simplified set for demonstration)
# These permutations represent rotations of the cube faces (simplified for teaching purposes)
# You would need the full set of generators for a complete 2x2x2 implementation.
F = Permutation(9, 11, 12, 10)(7, 20, 14, 21)(8, 18, 13, 23)
T = Permutation(5, 7, 8, 6)(4, 17, 9, 21)(3, 18, 10, 22)
D = Permutation(13, 15, 16, 14)(11, 19, 2, 23)(12, 20, 1, 24)
B = Permutation(1, 3, 4, 2)(17, 6, 24, 15)(19, 5, 22, 16)
L = Permutation(17, 19, 20, 18)(9, 5, 1, 13)(11, 7, 3, 15)
R = Permutation(21, 23, 24, 22)(10, 14, 2, 6)(12, 16, 4, 8)

# Define the group
G = PermutationGroup([F,T,D,B,L,R])

# Step 1: Display the full group generators
print("Group Generators:")
for gen in G.generators:
    print(f"  {gen.cyclic_form}")

# Step 2: Orbit Stabilizer Computation
base_points = [1,24]  # Example base for stabilizer computation
stabilizer_chain = []
group_order = 1

for i, point in enumerate(base_points):
    # Compute the orbit of the current point
    orbit = G.orbit(point)
    print(f"\nOrbit of point {point}: {orbit}")

    # Compute the stabilizer for the current point
    stabilizer = G.stabilizer(point)
    print(f"Stabilizer of point {point} size: {stabilizer.order()}")

    # Update group order and add stabilizer to the chain
    group_order *= len(orbit)
    stabilizer_chain.append(stabilizer)

# Step 3: Display the computed group order
print("\nStabilizer Chain:")
for i, stab in enumerate(stabilizer_chain):
    print(f"  G_{i+1}: Order = {stab.order()}")

print(f"\nComputed Group Order: {group_order}")

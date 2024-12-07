from rubiksCubeSolver import RubiksCubeSolver
from datetime import datetime
rubiksCubeSolver = RubiksCubeSolver()

state = {
    "T": [2, 1, 3, 1, 0, 5, 4, 4, 0],
    "L": [5, 5, 1, 5, 1, 3, 2, 4, 0],
    "F": [0, 1, 1, 2, 2, 1, 4, 0, 5],
    "R": [2, 4, 0, 0, 3, 3, 4, 0, 4],
    "B": [2, 2, 1, 4, 4, 2, 5, 3, 5],
    "D": [3, 3, 1, 0, 5, 2, 3, 5, 3]
}

start_time = datetime.now()
res = rubiksCubeSolver.solve(state)
print(len(res))
counter = []
for op in res:
    if op not in counter:
        counter.append(op)

print(counter)
print(datetime.now() - start_time)
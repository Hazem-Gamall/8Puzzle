from time import time
from heuristic import Heuristic, ManhttanDistance, NumberTiles
from puzzleState import PuzzleState
from puzzleSolver import PuzzleSolver, Greedy, HillClimbing, DEFAULT_GOAL 

solvable = [
    [2,3,4],
    [1,0,7],
    [8,6,5]
]

unsolvable = [
    [1,3,2],
    [4,5,6],
    [7,0,8]
]



def solve_puzzle(init, SolverClass:PuzzleSolver, HeuristicClass:Heuristic):
    heuristic = HeuristicClass()
    init_state = PuzzleState(init, heuristic.get_heuristic(init, DEFAULT_GOAL))
    solver = SolverClass(init_state, heuristic)
    return solver.solve()


avg = 0
for i in range(10):
    start = time()
    try:
        solve_puzzle(solvable, Greedy, ManhttanDistance)
    except Exception as e:
        print(e)
        break
    stop  = time()
    avg += stop-start

print("Greedy Avg time for h(n)=Manhattan Distance:")
print(avg/10)


avg = 0
for i in range(10):
    start = time()
    try:
        solve_puzzle(solvable, Greedy, NumberTiles)
    except Exception as e:
        print(e)
        break
    stop  = time()
    avg += stop-start

print("Greedy Avg time for h(n)=Number of misplaced tiles:")
print(avg/10)
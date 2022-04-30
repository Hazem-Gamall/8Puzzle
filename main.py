"""Solving the 8-Puzzle problem using the Greedy BFS and HillClimbing algorithim"""

import sys
from time import sleep, time
from heuristic import Heuristic, ManhttanDistance, NumberTiles
from puzzleState import PuzzleState
from puzzleSolver import PuzzleSolver, Greedy, HillClimbing, DEFAULT_GOAL 
from puzzle import Puzzle

def get_state_from_input(input):
    try:
        input = [int(i) for i in input] 
        if len(input) != 9:
            raise Exception("Invalid Length")

        for number in input:
            if number < 0 or number > 8:
                raise Exception(f'Incorrect input: {number}')
        state = []
        ind = 0
        for i in range(3):
            row = []
            for j in range(3):
                row.append(input[ind])
                ind+=1
            state.append(row)
            
        return state
    except Exception as e:
        print(e)
        
def solve_puzzle(init, SolverClass:PuzzleSolver, HeuristicClass:Heuristic):
    heuristic = HeuristicClass()
    init_state = PuzzleState(init, heuristic.get_heuristic(init, DEFAULT_GOAL))
    solver = SolverClass(init_state, heuristic)
    return solver.solve()

FILE = 1

def main():
    if len(sys.argv) > 1 and int(sys.argv[1]) == FILE:
        with open('input.txt', 'r') as file:
            numbers = file.readline()
            heuristic = ManhttanDistance if int(file.readline()) == 1 else NumberTiles
            state = get_state_from_input(numbers.split())
            print(state, heuristic)
            print(solve_puzzle(state, Greedy, heuristic))
    else:
        print("Please enter the puzzle numbers sperated by spaces(0 being the empty cell):")

        numbers = input()

        state = get_state_from_input(numbers.split())

        print("Choose which heuristic function you would like to use:")
        print("1-Manhattan Distance\t2-Number of misplaced tiles")
        heuristic = ManhttanDistance if int(input()) == 1 else NumberTiles

        print(solve_puzzle(state, Greedy, heuristic))

main()
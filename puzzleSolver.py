from puzzleState import PuzzleState
from queue import PriorityQueue
from heuristic import Heuristic

DEFAULT_GOAL = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]


class PuzzleSolver():
    def __init__(self, initial_state: PuzzleState, heuristic:Heuristic, goal = DEFAULT_GOAL) -> None:
        self.puzzle_state = initial_state
        self.goal = goal
        self.heuristic = heuristic 

    def solve():
        pass

class HillClimbing(PuzzleSolver):
    def __init__(self, initial_state: PuzzleState, heuristic:Heuristic,  goal = DEFAULT_GOAL) -> None:
        super().__init__(initial_state,heuristic ,goal)

    def solve(self, prev_move = ''):
        if self.puzzle_state.is_solvable():
            if self.puzzle_state.state == self.goal:
                # print(self.puzzle_state)
                # print('done')
                return self.puzzle_state
            self.puzzle_state.heuristic = self.heuristic.get_heuristic(self.puzzle_state.state, self.goal)
            moves = self.puzzle_state.allowed_moves(prev_move)
            queue = PriorityQueue()
            for move in moves:
                temp_state = PuzzleState(self.puzzle_state.make_move(move))
                temp_state.heuristic = self.heuristic.get_heuristic(temp_state.state, self.goal)
                # print(temp_state)
                queue.put((temp_state, move))
                
            # print('queue:', queue.queue)
            # print(self.puzzle_state)
            best_state = queue.get()
            if(best_state[0] > self.puzzle_state):
                # print(f"Stuck\nheuristic of current: {self.puzzle_state.heuristic}\nheuristic of best child:{best_state[0].heuristic}")
                # print('puzzle state:',self.puzzle_state)
                raise Exception('Hill Climbing Stuck')
            # sleep(1)
            self.puzzle_state = best_state[0]
            self.solve(best_state[1])
        else:
            raise Exception("Sorry puzzle instance is not solvable")

class Greedy(PuzzleSolver):
    def __init__(self, initial_state: PuzzleState, heuristic:Heuristic, goal = DEFAULT_GOAL) -> None:
        super().__init__(initial_state, heuristic, goal)
    
    def solve(self):
        if(self.puzzle_state.is_solvable()):
            new_states = PriorityQueue() 
            prev_move=''
            visited =[]
            num_expansions = 0
            while new_states:
                if self.puzzle_state.state == self.goal:
                    # print('num_expansions:',num_expansions)
                    # print('queue elements:', len(new_states.queue))
                    # print('done')
                    # print(self.puzzle_state)
                    return self.puzzle_state
                moves = self.puzzle_state.allowed_moves(prev_move)
                
                for move in moves:
                    temp_state = PuzzleState(self.puzzle_state.make_move(move))
                    temp_state.heuristic = self.heuristic.get_heuristic(temp_state.state, self.goal)

                    if temp_state.state not in visited:
                        num_expansions +=1

                        new_states.put((temp_state, move))
                        visited.append(temp_state.state)

                min_distance = new_states.get()

                self.puzzle_state = min_distance[0]
                prev_move=min_distance[1]
        else:
            raise Exception("Sorry puzzle instance is not solvable")

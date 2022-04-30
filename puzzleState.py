import copy

class PuzzleState():
    def __init__(self, init, heuristic = 0) -> None:
        self.__state = init
        self.__heuristic = heuristic

    def is_solvable(self):
        flat_mat = [element for row in self.__state for element in row]
        
        inversion = 0
        for i in range(len(flat_mat)):
            for j in range(i+1, len(flat_mat)):
                if flat_mat[i] != 0 and flat_mat[j] != 0:
                        if flat_mat[i] > flat_mat[j]:
                            inversion+=1
                            # print(i,j)
        if inversion%2 == 0:
            return True
        else:
            return False

    def get_cords_of(self, element):
        for i in range(len(self.__state)):
            for j in range(len(self.__state[i])):
                if(self.__state[i][j] == element):
                    return (i,j)
        raise Exception("Element not found")

    def swap(self, state, cord1, cord2):
        state[cord1[0]][cord1[1]], state[cord2[0]][cord2[1]] = state[cord2[0]][cord2[1]],state[cord1[0]][cord1[1]]

    def allowed_moves(self, prev_move):
        empty_cell_cords = self.get_cords_of(0)
        moves = []
        # print(empty_cell_cords)
        if empty_cell_cords[0] + 1 < len(self.__state) and prev_move != "UP":# and prev_move != "DOWN":
            moves.append('DOWN')
        if empty_cell_cords[0] -1 > -1 and prev_move != "DOWN" :#and prev_move != "DOWN"):
            moves.append('UP')
        if empty_cell_cords[1] +1 < len(self.__state) and prev_move != "LEFT":# and prev_move != "RIGHT":
            moves.append('RIGHT')
        if empty_cell_cords[1] -1 > -1 and prev_move != "RIGHT":#and prev_move != "RIGHT":
            moves.append('LEFT')
        return moves

        
    def make_move(self, move):
        # print(copy_mat is mat)
        empty_cords = self.get_cords_of(0)

        if move == 'UP':
            new_cords = list(empty_cords)
            new_cords[0] -= 1
        elif move == 'DOWN':
            new_cords = list(empty_cords)
            new_cords[0] += 1
        elif move == 'RIGHT':
            new_cords = list(empty_cords)
            new_cords[1] += 1
        elif move == 'LEFT':
            new_cords = list(empty_cords)
            new_cords[1] -= 1

        copy_mat = copy.deepcopy(self.__state)
        self.swap(copy_mat, empty_cords, new_cords)
        return copy_mat

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        self.__state = new_state

    @property
    def heuristic(self):
        return self.__heuristic

    @heuristic.setter
    def heuristic(self, new_state):
        self.__heuristic = new_state

    def __lt__(self, other):
        return self.__heuristic < other.heuristic

        
    def __str__(self) -> str:
        result = f'heuristic: {self.__heuristic}\n'
        for row in self.__state:
            for element in row:
                result += f'{element}   '
            result+='\n'
        return result


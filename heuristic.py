class Heuristic():
    def get_heuristic(self, mat1, mat2) -> int:
        pass

class ManhttanDistance(Heuristic):
    def manhattan_formula(self, cord1, cord2):
        # print(cord1, cord2)
        return (abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1]))

    def elements_locations(self, mat):
        locations = {}
        # print(goal[0][1])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # print(goal[i][j])
                locations[mat[i][j]] = (i,j)
        return locations
    #O(nm)
    def get_heuristic(self,mat1, mat2):
        goal_locations = self.elements_locations(mat2)
        # print(goal_locations)
        sum = 0
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                if mat1[i][j] == 0:
                    continue
                # print(f'goal_locations[{mat1[i][j]}]:', goal_locations[mat1[i][j]])
                sum += self.manhattan_formula(goal_locations[mat1[i][j]], (i,j))

        return sum

class NumberTiles(Heuristic):

    def get_heuristic(self,mat1, mat2):
        num_tiles = 0
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                if mat1[i][j] == 0:
                    continue
                if mat1[i][j] != mat2[i][j]:
                    num_tiles+=1
        return num_tiles

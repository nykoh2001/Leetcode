# 11:32 ~ 11:56

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row_count = len(boxGrid)
        col_count = len(boxGrid[0])

        walls = {}

        for r in range(row_count):
            stones = 0
            for c in range(col_count):
                if boxGrid[r][c] == "#":
                    stones += 1
                if boxGrid[r][c] == "*":
                    walls[(r, c)] = stones
                    stones = 0
            if stones:
                walls[(r, col_count)] = stones

        rotated = [["."] * row_count for _ in range(col_count)]
        for wall, stone_count in walls.items():
            rotated_wall_r, rotated_wall_c = wall[1], row_count - 1 - wall[0]

            if rotated_wall_r in range(0, col_count):
                rotated[rotated_wall_r][rotated_wall_c] = "*"
            for i in range(1, stone_count + 1):
                rotated[rotated_wall_r - i][rotated_wall_c] = "#"
        return rotated

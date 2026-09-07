import heapq as hq


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        dr_dc = [(1, 0), (0, 1)]
        cost_per_cell = {}
        m, n = len(grid), len(grid[0])
        last_cell = (m - 1, n - 1)
        for r in range(m):
            for c in range(n):
                cost_per_cell[(r, c)] = grid[r][c]

        def getAdjacentCells(r: int, c: int):
            cells = []
            for dr, dc in dr_dc:
                new_r = r + dr
                new_c = c + dc
                if new_r not in range(0, m) or new_c not in range(0, n):
                    continue

                cells.append((new_r, new_c))

            return cells

        distances = [[10 ** 9] * n for _ in range(m)]
        cell_to_visit = [(0, 0, 0)]
        while cell_to_visit:
            r, c, cost = hq.heappop(cell_to_visit)

            new_cost = cost + cost_per_cell[(r, c)]
            if new_cost >= distances[r][c]:
                continue

            distances[r][c] = new_cost

            if (r, c) == last_cell:
                continue
            adjacent_cells = getAdjacentCells(r, c)
            for next_r, next_c in adjacent_cells:
                hq.heappush(cell_to_visit, (next_r, next_c, new_cost))

        return distances[m - 1][n - 1]

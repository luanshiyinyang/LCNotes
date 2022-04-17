class Solution:

    def __init__(self):
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    # 开始dfs
                    stack = [(i, j)]
                    seen = set()
                    seen.add((i, j))
                    while stack:
                        node = stack.pop()
                        for nx, ny in self.dirs:
                            newx, newy = node[0] + nx, node[1] + ny
                            if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in seen and grid[newx][newy] == 1:
                                stack.append((newx, newy))
                                seen.add((newx, newy))
                    visited |= seen
                    res.append(seen)

        # 按照题意，这里的res的长度一定是2
        source = res[0]
        queue = collections.deque([(node, 0) for node in source])
        target = res[1]
        while queue:
            node, d = queue.popleft()
            if node in target: return d - 1
            for nx, ny in self.dirs:
                newx, newy = node[0] + nx, node[1] + ny
                if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in source:
                    queue.append(((newx, newy), d + 1))
                    source.add((newx, newy))
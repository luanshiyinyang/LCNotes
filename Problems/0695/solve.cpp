class Solution
{
public:
    const int dx[4] = {1, 0, 0, -1};
    const int dy[4] = {0, 1, -1, 0};
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int res = 0;
        for (int x = 0; x < grid.size(); x++)
        {
            for (int y = 0; y < grid[0].size(); y++)
            {
                res = max(res, dfs(grid, x, y));
            }
        }
        return res;
    }

    int dfs(vector<vector<int>> &grid, int x, int y)
    {
        int res = 0;
        if (grid[x][y] == 1)
        {
            grid[x][y] = 0;
            res++;
            for (int i = 0; i < 4; i++)
            {
                int mx = x + dx[i], my = y + dy[i];
                if (mx >= 0 && my >= 0 && mx < grid.size() && my < grid[0].size())
                {
                    res += dfs(grid, mx, my);
                }
            }
        }
        return res;
    }
};

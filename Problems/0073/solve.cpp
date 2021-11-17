class Solution
{
public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        unordered_set<int> rowSet, colSet;
        for (int i = 0; i < matrix.size(); i++)
        {
            for (int j = 0; j < matrix[0].size(); j++)
            {
                if (matrix[i][j] == 0)
                {
                    rowSet.insert(i);
                    colSet.insert(j);
                }
            }
        }
        for (int x : rowSet)
        {
            for (int i = 0; i < matrix[0].size(); i++)
            {
                matrix[x][i] = 0;
            }
        }
        for (int y : colSet)
        {
            for (int i = 0; i < matrix.size(); i++)
            {
                matrix[i][y] = 0;
            }
        }
    }
};

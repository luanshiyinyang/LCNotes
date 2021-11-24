class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int m = matrix.size(), n = matrix[0].size(), rowLeft = 0, rowRight = m - 1, mid = 0, row = mid;
        while (rowLeft <= rowRight)
        {
            mid = rowLeft + (rowRight - rowLeft) / 2;
            if (matrix[mid][0] <= target && matrix[mid][n - 1] >= target)
            {
                break;
            }
            if (matrix[mid][0] > target)
            {
                rowRight = mid - 1;
            }
            else if (matrix[mid][n - 1] < target)
            {
                rowLeft = mid + 1;
            }
        }
        row = mid;
        int colLeft = 0, colRight = n - 1;
        while (colLeft <= colRight)
        {
            int mid = colLeft + (colRight - colLeft) / 2;
            if (matrix[row][mid] == target)
            {
                return true;
            }
            if (matrix[row][mid] > target)
            {
                colRight = mid - 1;
            }
            else if (matrix[row][mid] < target)
            {
                colLeft = mid + 1;
            }
        }
        return false;
    }
};

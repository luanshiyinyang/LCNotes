class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> res(r);
        if (m * n != r * c){
            return mat;
        }
        for (int i = 0; i < m * n; i++) {
            if (i % c == 0) {
                res[i / c].resize(c);
            }
            res[i / c][i % c] = mat[i / n][i % n];
        }
        return res;
    }
};

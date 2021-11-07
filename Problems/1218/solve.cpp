class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int, int> dp;
        int res = 0;
        for(int num : arr){
            dp[num] = dp[num - difference] + 1;
            res = max(res, dp[num]);
        }
        return res;
    }
};

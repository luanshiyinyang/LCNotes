class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = 0, res = INT_MIN;
        for(int num : nums){
            pre = max(pre + num, num);
            res = max(res, pre);
        }
        return res;
    }
};

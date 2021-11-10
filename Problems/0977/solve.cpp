class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int i = 0, j = nums.size() - 1, pos = nums.size() - 1;
        vector<int> res(nums.size());
        while(i <= j && pos >= 0){
            if (nums[i] * nums[i] >= nums[j] * nums[j]){
                res[pos--] = nums[i] * nums[i];
                i++;
            } else {
                res[pos--] = nums[j] * nums[j];
                j--;
            }
        }
        return res;
    }
};

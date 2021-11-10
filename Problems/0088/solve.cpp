class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> nums(m + n);
        int i = 0, j = 0;
        while(i < m || j < n){
            if(i == m){
                nums[i + j] = nums2[j];
                j++;
            } else if(j == n){
                nums[i + j] = nums1[i];
                i++;
            } else if (nums1[i] <= nums2[j]) {
                nums[i + j] = nums1[i];
                i++;
            } else {
                nums[i + j] = nums2[j];
                j++;
            }
        }
        nums1.swap(nums);
    }
};

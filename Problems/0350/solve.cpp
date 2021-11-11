class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> myMap;
        vector<int> res;
        for (int num1 : nums1) {
            auto it = myMap.find(num1);
            if (it != myMap.end()) {
                it->second++;
            } else {
                myMap[num1] = 1;
            }
        }
        for (int num2 : nums2) {
            auto it = myMap.find(num2);
            if (it != myMap.end() && it->second > 0) {
                res.push_back(num2);
                it->second--;
            }
        }
        return res;
    }
};

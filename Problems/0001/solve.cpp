class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> myMap;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            unordered_map<int, int>::iterator it = myMap.find(target - nums[i]);
            if(it != myMap.end()){
                res.push_back(i);
                res.push_back(it->second);
                break;
            }
            myMap[nums[i]] = i;
        }
        return res;
    }
};

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> myMap;
        for(int num : nums){
            if(myMap.find(num) != myMap.end()){
                return true;
            }
            myMap.insert(num);
        }
        return false;
    }
};

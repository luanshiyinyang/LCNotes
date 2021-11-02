class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> mySet(candyType.begin(), candyType.end());
        return min(candyType.size() / 2, mySet.size());
    }
};
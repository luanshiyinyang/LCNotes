class Solution
{
public:
    int subarraySum(vector<int> &nums, int k)
    {
        int res = 0;
        vector<int> sum;
        unordered_map<int, int> myMap;
        sum.push_back(0);
        for (int x : nums)
        {
            sum.push_back(sum.back() + x);
        }
        for (int i = sum.size() - 1; i >= 0; i--)
        {
            if (myMap.find(sum[i]) != myMap.end())
                res += myMap[sum[i]];
            else
                myMap[sum[i] - k]++;
        }
        return res;
    }
};

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_map<char, int> myMap;
        for (auto c : s)
        {
            myMap[c]++;
        }
        for (auto c : t)
        {
            myMap[c]--;
        }
        for (auto x : myMap)
        {
            if (x.second != 0)
            {
                return false;
            }
        }
        return true;
    }
};

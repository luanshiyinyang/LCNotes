class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        unordered_map<char, int> myMap;
        for (auto c : magazine)
        {
            myMap[c]++;
        }
        for (auto c : ransomNote)
        {
            if (myMap[c] == 0)
            {
                return false;
            }
            myMap[c]--;
        }
        return true;
    }
};

class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> stk;
        unordered_map<char, char> myMap = {{')', '('}, {']', '['}, {'}', '{'}};
        for (auto x : s)
        {
            if (myMap.find(x) == myMap.end())
            {
                stk.push(x);
            }
            else if (stk.size() != 0 && myMap[x] == stk.top())
            {
                stk.pop();
            }
            else
            {
                return false;
            }
        }
        return stk.empty();
    }
};

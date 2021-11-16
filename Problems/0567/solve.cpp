class Solution
{
public:
    bool checkInclusion(string s1, string s2)
    {
        vector<int> ch1(26), ch2(26);
        int m = s1.size(), n = s2.size();
        if (m > n)
            return false;
        for (int i = 0; i < m; i++)
        {
            ch1[s1[i] - 'a']++;
            ch2[s2[i] - 'a']++;
        }
        if (ch1 == ch2)
        {
            return true;
        }
        for (int j = m; j < n; j++)
        {
            ch2[s2[j - m] - 'a']--;
            ch2[s2[j] - 'a']++;
            if (ch1 == ch2)
            {
                return true;
            }
        }
        return false;
    }
};

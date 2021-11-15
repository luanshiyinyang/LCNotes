class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0, right = 0, res = 0;
        string t("");
        while (right < s.size()){
            while (t.find(s[right]) != string::npos) {
                t.erase(0, 1);
                left--;
            }
            t.insert(t.end(), s[right]);
            right++;
            res = max(res, right - left);
        }
        return res;
    }
};

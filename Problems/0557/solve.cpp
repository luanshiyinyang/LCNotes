class Solution {
public:
    string reverseWords(string s) {
        int i = 0, left, right;
        while (i < s.size()) {
            left = i;
            while (s[i] != ' ' && i < s.size()) {
                i++;
            }
            right = i - 1;
            while (left < right){
                swap(s[left++], s[right--]);
            }
            i++;
        }
        return s;
    }
};

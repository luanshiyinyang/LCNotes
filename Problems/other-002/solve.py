class Solution(object):
    def solve(self, s: str):
        flag, num = 0, 0
        for i in range(len(s)):
            if s[i] == 'c':
                num += (i - flag)
                flag += 1
        return num
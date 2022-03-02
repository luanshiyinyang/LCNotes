class Solution:
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_len, begin = 1, 0
        for l in range(2, n + 1):
            for i in range(n):
                j = l + i - 1
                if j >= n: break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and l > max_len:
                    max_len = l
                    begin = i
        return s[begin:begin + max_len]

    def longestPalindrome2(self, s: str) -> str:
        end, start, r, j = -1, 0, -1, -1
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = [0] * len(s)
        print(s)
        for i in range(len(s)):
            # arm_len[i] = 1 if i >= r else min(arm_len[2 * j - i], r - i)
            # while i - arm_len[i] >= 0 and i + arm_len[i] <= len(s) - 1 and s[i - arm_len[i]] == s[i + arm_len[i]]:
            #     arm_len[i] += 1

            if i >= r:
                arm_len[i] = 1
                while i - arm_len[i] >= 0 and i + arm_len[i] <= len(s) - 1 and s[i - arm_len[i]] == s[i + arm_len[i]]:
                    arm_len[i] += 1
            else:
                if arm_len[j * 2 - i] > r - i:
                    arm_len[i] = r - i 
                elif arm_len[j * 2 - i] < r - i:
                    arm_len[i] = arm_len[j * 2 - i]
                else:
                    arm_len[i] = r - i 
                    while i - arm_len[i] >= 0 and i + arm_len[i] <= len(s) - 1 and s[i - arm_len[i]] == s[i + arm_len[i]]:
                        arm_len[i] += 1


            if i + arm_len[i] > r:
                r = i + arm_len[i]
                j = i
            if arm_len[i] * 2 > end - start:
                start, end = i - arm_len[i], i + arm_len[i]
        return s[start+2:end-1:2]
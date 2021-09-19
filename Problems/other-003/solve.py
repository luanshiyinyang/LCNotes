from typing import List


def cal(num, i, j):
    # 计算num的i位到j位组成的十进制数
    value = 0
    while j >= i:
        value = value * 10 + num[i]
        i = i + 1
    return value


def solve(num: List[int], n, k):
    if k > n:
        return 0
    dp = [[0] * k for _ in range(n)]
    # 对于任何前i位拆为一段，最大乘积都是本身
    for i in range(n):
        dp[i][0] = cal(num, 0, i)

    for j in range(1, k):
        for i in range(j, n):
            dp[i][j] = max([dp[m][j - 1] * cal(num, m + 1, i) for m in range(i)])

    return dp[n - 1][k - 1]


print(solve([2, 3, 4, 2], 4, 2))  # 2342 to 23 * 42

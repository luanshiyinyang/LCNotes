class Solution(object):
    def solve(self, n: int, k: int, a: list):
        accu = [a[-1]]
        # 累加后缀和
        for i in range(1, n):
            accu.append(accu[i - 1] + a[-(i + 1)])
        ans = accu[-1]  # 必有原始数组
        accu.pop(-1)
        accu.sort(reverse=True)  # 降序排列
        ans += sum(accu[:(k - 1)])  # 原始数组加上最大的k-1个后缀和
        return ans
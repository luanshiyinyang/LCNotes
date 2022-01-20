import collections

class Solution:
    def permutation1(self, s: str) -> list[str]:
        s = list(s)
        pool = collections.deque()
        pool.append(s[0])
        i = 1
        while i <= len(s) - 1:
            ins = s[i]
            while len(pool[0]) == i:
                temp = list(pool.popleft())
                for index in range(0, i + 1):
                    tempi = temp.copy()
                    tempi.insert(index, ins)
                    tempi = ''.join(tempi)
                    if tempi not in pool:
                        pool.append(tempi)
            i += 1
        return list(pool)

    def permutation2(self, s: str) -> list[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res
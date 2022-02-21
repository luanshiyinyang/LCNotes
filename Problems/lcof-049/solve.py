import heapq

class Solution:
    def nthUglyNumber1(self, n: int) -> int:
        # 最小堆
        ugly = [2, 3, 5]
        heap = [1]
        uglys = [1]
        for _ in range(n - 1):
            small = heapq.heappop(heap)
            for u in ugly:
                if small * u not in uglys:
                    heapq.heappush(heap, small * u)
                    uglys.append(small * u)
        return heapq.heappop(heap)

    def nthUglyNumber2(self, n: int) -> int:
        ans = [0] * (n + 1)
        p2, p3, p5 = 1, 1, 1
        ans[1] = 1
        for i in range(2, n + 1):
            num2, num3, num5 = ans[p2] * 2, ans[p3] * 3, ans[p5] * 5
            num = min(num2, num3, num5)
            ans[i] = num
            if num == num2:
                p2 += 1
            if num == num3:
                p3 += 1
            if num == num5:
                p5 += 1
        # print(ans)
        return ans[n]
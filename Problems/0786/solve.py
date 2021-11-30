class Frac:
    def __init__(self, idx: int, idy: int, x: int, y: int) -> None:
        self.idx = idx
        self.idy = idy
        self.x = x
        self.y = y

    def __lt__(self, other: "Frac") -> bool:
    # python中的富比较方法，用于类之间的比较，比如对类的不同实例进行sort。
        return self.x * other.y < self.y * other.x


class Solution:
    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        # heapq是python中的用于实现堆的一个模块heapqify是将列表具有堆特征。
        heapq.heapify(q)
		
        for _ in range(k - 1):
            frac = heapq.heappop(q)
            i, j = frac.idx, frac.idy
            if i + 1 < j:
            	# 将arr[i + 1] / arr[j]放入优先队列中
                heapq.heappush(q, Frac(i + 1, j, arr[i + 1], arr[j]))
        
        return [q[0].x, q[0].y]
        
    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
    	n = len(arr)
        left, right = 0.0, 1.0
        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            x, y = 0, 1
            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > x * arr[j]:
                        x, y = arr[i], arr[j]
                count += i + 1
            if count == k: return [x, y]
            if count < k:
                left = mid
            if count > k:
                right = mid
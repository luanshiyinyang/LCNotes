class Solution:
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        juli = [[float("inf")] * n for _ in range(k + 2)]
        juli[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                juli[t][i] = min(juli[t][i], juli[t - 1][j] + cost)
        mincost = min(juli[t][dst] for t in range(1, k + 2))
        if mincost == float("inf"):
            return -1
        else: 
            return mincost
    
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        juli1 = [float("inf")] * n 
        juli1[src] = 0
        mincost = float('inf')
        for t in range(1, k + 2):
            juli2 = [float("inf")] * n 
            for j, i, cost in flights:
                juli2[i] = min(juli2[i], juli1[j] + cost)
            juli1 = juli2
            mincost = min(mincost, juli1[dst])
        if mincost == float("inf"):
            return -1
        else: 
            return mincost
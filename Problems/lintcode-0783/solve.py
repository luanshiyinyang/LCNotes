class Solution:
    """
    @param n: maximum index of position.
    @param m: the number of undirected edges.
    @param x: 
    @param y: 
    @param w: 
    @return: return the minimum risk value.
    """
    def get_min_risk_value(self, n: int, m: int, x: List[int], y: List[int], w: List[int]) -> int:
        # 建图
        adj = collections.defaultdict(list)
        for i in range(m):
            adj[x[i]].append((y[i], w[i]))
            adj[y[i]].append((x[i], w[i]))
        print(adj)
        MST = collections.defaultdict(list)
        min_heap = [(w, 0, v) for v, w in adj[0]]
        heapq.heapify(min_heap)

        while n not in MST:
            w, p, v = heapq.heappop(min_heap)
            if v not in MST:
                MST[p].append((v, w))
                MST[v].append((p, w))
                for k, w in adj[v]:
                    if k not in MST:
                        heapq.heappush(min_heap, (w, v, k))
        
        dfs = [(0, None, float('-inf'))]
        while dfs:
            v, p, max_w = dfs.pop()
            for k, w in MST[v]:
                cur_max_w = max(max_w, w)
                if k == n:
                    return cur_max_w
                if k != p:
                    dfs.append((k, v, cur_max_w))
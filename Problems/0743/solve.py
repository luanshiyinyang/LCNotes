class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)
        for start, end, time in times:
            g[start].append((end, time))
        
        # 生成最短路径树SPT
        SPT = {}
        min_heap = [(0, k)]
        while min_heap:
            duration, node = heappop(min_heap)
            if node not in SPT:
                SPT[node] = duration
                for adj_node, adj_node_duration in g[node]:
                    if adj_node not in SPT:
                        heappush(min_heap, (adj_node_duration + duration, adj_node))
        return max(SPT.values()) if len(SPT) == n else -1
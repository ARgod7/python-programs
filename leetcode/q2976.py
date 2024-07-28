from collections import defaultdict
import heapq


def minimumCost(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        adj = defaultdict(list)
        for src, dst, cur_cost in zip(original, changed, cost):
            adj[src].append((dst, cur_cost))
        
        def dijkstra(src):
            heap = [(0, src)]
            cmap = {}
            
            while heap:
                cost, node = heapq.heappop(heap)
                if node in cmap:
                    continue
                cmap[node] = cost
                for nei, neiCost in adj[node]:
                    heapq.heappush(heap, (cost + neiCost, nei))
                return cmap
        
        costMap = {c:dijkstra(c) for c in set(source)}
        res = 0
        for src, dst in zip(source, target):
            if dst not in costMap[src]:
                return -1
            res += costMap[src][dst]
        return res

        
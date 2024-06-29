from collections import defaultdict, deque


def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        ancestors = [set() for _ in range(n)]
        incoming = [0]*(n)

        for start, end in edges:
            graph[start].append(end)
            ancestors[end].add(start)
            incoming[end]+=1
        
        q = deque()
        for node in range(n):
            if not incoming[node]:
                q.append(node)
                
        while q:
            node = q.popleft()
            for adjacent_node in graph[node]:
                ancestors[adjacent_node].update(ancestors[node])
                incoming[adjacent_node] -=1
                if not incoming[adjacent_node]:
                    q.append(adjacent_node)

        result = []
        for node in range(n):
            result.append(sorted(ancestors[node]))
        return result


        # pathMap = defaultdict(list)
        # for i , j in edges:
        #     pathMap[j].append(i)
        
        # def dfs(i):
        #     for x in pathMap[i]:
        #         if x not in visited:
        #             visited.add(x)
        #             dfs(x)
        
        # d = defaultdict(list)
        # for k in range(n):
        #     visited = set()
        #     dfs(k)
        #     d[k] = sorted(list(visited))
        # return list(d.values())


getAncestors(8,[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])
        
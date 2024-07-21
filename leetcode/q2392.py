from collections import defaultdict


def buildMatrix( k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if  not dfs(nei, adj, visit, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True
            

        
        def topoSort(edge):
            adj = defaultdict(list)
            for src , des in edge:
                adj[src].append(des)

            visit ,  path = set() , set()
            order = []

            for src in range(1, k+1):
                if not dfs(src, adj, visit, path, order):
                    return  []

            return order[::-1]
        
        row_order = topoSort(rowConditions)
        col_order = topoSort(colConditions)

        if not row_order or not col_order:
            return []
        
        rowValue = {n:i for i, n in enumerate(row_order)}
        colValue = {n:i for i, n in enumerate(col_order)}

        res = [[0] * k for _ in range(k)]
        for num in range(1, k+1):
            r , c = rowValue[num], colValue[num]
            res[r][c] = num
        return res
        
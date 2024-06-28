def maximumImportance(n: int, roads: list[list[int]]) -> int:
        count = [0] * n
        for n1 , n2 in roads:
            count[n1] += 1
            count[n2] += 1
        
        label = 1
        res = 0
        for n in sorted(count):
            res += label * n
            label += 1
        return res

maximumImportance(5,[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
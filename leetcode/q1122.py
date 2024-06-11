from typing import Counter


def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
        count = Counter(arr1)
        arr2_set = set(arr2)

        end = []

        for i in arr1:
            if i not in arr2_set:
                end.append(i)
        
        print(end)
        res = []

        for n in arr2:
            for _ in range (count[n]):
                res.append(n)
        
        print(res+end)
        
relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31],[2,42,38,0,43,21])
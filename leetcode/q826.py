def maxProfitAssignment(diff: list[int], profit: list[int], worker: list[int]) -> int:
        md = max(diff)
        count = [0]*(md+1)
        for n in range (len(diff)):
            count[diff[n]] = max(count[diff[n]],profit[n])

        for i in range(1,(md+1)):
            count[i] = max(count[i],count[i-1])

        res = 0
        for w in worker:
            if w <= md:
                res += count[w]
            else:
                 res += count[md]
        return res
             

maxProfitAssignment([13,37,58],[4,90,96],[34,73,45])
        
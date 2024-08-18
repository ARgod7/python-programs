def nthUglyNumber( n: int) -> int:
        num = [1]
        i2, i3, i5 = 0, 0, 0

        for i in range(1, n):
            next_num = min(num[i2]*2, num[i3]*3, num[i5]*5)
            num.append(next_num)
            if next_num == num[i2]*2:
                i2 += 1
            if next_num == num[i3]*3:
                i3 += 1
            if next_num == num[i5]*5:
                i5 += 1
        return num[n - 1]
        # visit = set()
        # factors = [ 2, 3, 5 ]
        # for i in range(n):
        #     num = heapq.heappop(minHeap)
        #     if i == n - 1:
        #         return num
        #     for f in factors:
        #         if num * f not in visit:
        #             visit.add( num * f )
        #             heapq.heappush(minHeap, num*f)     
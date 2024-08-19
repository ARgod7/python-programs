def minSteps( n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n = n/d
            d += 1
        return ans
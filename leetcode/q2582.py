def passThePillow(n: int, time: int) -> int:
        time %= (n-1)*2
        if time < n:
            return 1 + time
        return n - (time - (n - 1))
print(passThePillow(8,50))
        
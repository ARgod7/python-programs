def isPowerOfTwo(n: int) -> bool:
        # if n == 1:
        #     return True
        # elif n < 1:
        #     return False
        # else:
        #     return self.isPowerOfTwo(n/2)
        return n > 0 and ((1 << 30) % n) == 0
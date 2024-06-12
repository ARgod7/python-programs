# def myPow(x: float, n: int) -> float:
#     if x == 0:
#         return 0
#     if n == 0:
#         return 1
#     res = 1
#     for _ in range(abs(n)):
#         res = res * x

#     return res if n>=0 else 1/res

# print(myPow(0,0))

def myPow(x: float, n: int) -> float:
        def rec(x,n):
            if x == 0: return 0
            if n == 0: return 1

            res = rec(x , n // 2)
            res = res * res
            return x * res if n%2 else res

        
        res = rec(x , abs(n))
        return res if n>=0 else 1/res

print(myPow(6,6))
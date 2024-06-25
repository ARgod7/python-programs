def isPowerOfThree( n: int) -> bool:
    x = 0
    while n>=3:
        if(n % 3 != 0) : return False
        n = n/3
        x += 1
    return [True,x]
isPowerOfThree(0)
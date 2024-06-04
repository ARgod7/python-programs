# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

import math



def reverse(self, x: int) -> int:
        res = 0
        min = -2147483648
        max = 2147483647

        while(x!=0):
            rem = int(math.fmod(x,10))
            x = int(x/10)

            if(res > int(max/10) or (res == int(max/10) and rem >= int(math.fmod(max,10)))):
                return 0
            if(res < int(min/10) or (res == int(max/10) and rem <= int(math.fmod(min,10)))):
                return 0
        
            res = res*10 + rem

        return res




# METHOD 2
def reverse(x: int) -> int:
        strev = str(x)[::-1]
        if strev[-1] == "-":
            val = -int(strev[:-1])
        else:
            val = int(strev)
        
        if val < -2 ** 31 or val > 2 ** 31 - 1:
            return 0
        else:
            return val
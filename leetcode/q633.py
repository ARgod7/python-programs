# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:

# Input: c = 3
# Output: false

from cmath import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l , r = 0 , int(sqrt(c))
        while l<=r:
            t = (l * l) + (r * r)
            if t < c:
                l += 1
            elif t > c:
                r -= 1
            else:
                return True
        return False
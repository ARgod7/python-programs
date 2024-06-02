# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a , b = a[::-1] , b[::-1]
        
        for i in range(max(len(a),len(b))):
            numA = int(a[i]) if i < len(a) else 0
            numB = int(b[i]) if i < len(b) else 0
            val = numA + numB + carry

            carry = val//2
            char = str(val%2)
            res = char + res

        if carry == 1:
            res = "1" + res
        return res



        
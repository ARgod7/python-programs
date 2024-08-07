# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

 

# Example 1:

# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:

# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
# Example 3:

# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

def reverseParentheses(s: str) -> str:
        res = []
        for c in s:
            if c == ")":
                temp = []
                while res[-1] != "(":
                    temp.append(res.pop())
                res.pop()
                res.extend(temp)
            else:
                res.append(c)
        return "".join(res)
        
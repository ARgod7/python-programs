# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


def isValid(s: str) -> bool:
        stack = []
        checkmap = { ")" : "(" , "]" : "[" , "}" : "{" }

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack or stack.pop() != checkmap[c]:
                    return False

        return len(stack) == 0
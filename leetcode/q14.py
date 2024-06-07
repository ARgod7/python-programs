# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs: list[str]) -> str:
        
        strs.sort()

        first = strs[0]
        last = strs[len(strs)-1]

        i = 0
        res = ""

        while i < len(first) and i < len(last):
            if first[i] != last[i]:
                break
            res += first[i]
            i += 1

        return res

print(longestCommonPrefix(["flower","flow","flight"]))




# mini,maxi=min(strs),max(strs)

#         for i in range(len(mini)):
#             if mini[i]!=maxi[i]:
#                 return mini[:i]
#         return mini
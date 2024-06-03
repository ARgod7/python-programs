def lengthOfLongestSubstring(s) -> int:
        l = res = 0
        map = {}
        
        for r in range(len(s)):
            if s[r] in map and l <= map[s[r]]:
                l = map[s[r]] + 1
            else:
                res = max(res, r - l + 1)
            map[s[r]] = r
        return res

ans = lengthOfLongestSubstring("pwwkew")
print(ans)
    




        
def myAtoi(s: str) -> int:

        s = s.replace(" ","")

        if not s :
            return 0
        
        i = 0
        sign = 1
        num = 0

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            sign = -1
        
        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                num = num * 10 + int(s[i])
            i += 1
        
        num *= sign
        if num < 0:
            return (max(num,-2**31))
        return (min(num,2**31 - 1))

print(myAtoi("+-12"))

        
        
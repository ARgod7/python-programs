def minOperations(logs: list[str]) -> int:
        res = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                res -= 1 if res > 0 else 0
            else:
                res += 1
        return res
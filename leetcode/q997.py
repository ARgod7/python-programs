def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # check = defaultdict(int)
        # for a, b in trust:
        #     check[a] -= 1
        #     check[b] += 1
        # for i in range(1, n+1):
        #     if check[i] == n-1:
        #         return i
        # return -1
        if n == 1:
            return 1 if not trust else -1
        people = [0] * (n+1)
        judge = [0] * (n+1)
        for t in trust:
            people[t[0]] += 1
            judge[t[1]] += 1
        for i in range(1 , n + 1):
            if people[i] == 0 and judge[i] == n-1:
                return i
        return -1

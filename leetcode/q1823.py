from collections import deque


def findTheWinner(n: int, k: int) -> int:
        # res = 0
        # for x in range(1, n+1):
        #     res = (res + k) % x
        # return res + 1

        q = deque()
        for i in range(1 , n + 1):
            q.append(i)
        while len(q) > 1:
            for i in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q[0]

        # def helper(n,k):
        #     if n == 1:
        #         return 0
        #     return (helper(n-1,k) + k) % n
        # return helper(n,k) + 1
findTheWinner(5,2)

        
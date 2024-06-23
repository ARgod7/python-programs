from sortedcontainers import SortedList # type: ignore
from collections import deque

def longestSubarray(self, nums: list[int], limit: int) -> int:
        # n = len(nums)
        # sl = SortedList()
        # best = 0
        # l = 0
        # for r in range(n):
        #     sl.add(nums[r])
        #     while(sl[-1] - sl[0] > limit):
        #         sl.remove(nums[l])
        #         l += 1
        #     best = max(best, r - l + 1)
        # return best
        max_queue = deque()  
        min_queue = deque() 

        left = 0

        for n in nums:
            while max_queue and n > max_queue[-1]:
                max_queue.pop()
            max_queue.append(n)
            while min_queue and n < min_queue[-1]:
                min_queue.pop()
            min_queue.append(n)
            if max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1
        return len(nums) - left
        
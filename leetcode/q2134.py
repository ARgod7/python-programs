def minSwaps(self, nums: list[int]) -> int:
        # n = len(nums)
        # total_ones = nums.count(1)
        # l = 0
        # max_win_one = win_one = 0
        # for r in range(2 * n):
        #     if nums[r % n]:
        #         win_one += 1
        #     if r - l + 1 > total_ones:
        #         win_one -= nums[l % n]
        #         l += 1
        #     max_win_one = max(max_win_one, win_one)
        # return total_ones - max_win_one
        total = sum(nums)
        nums.extend(nums)
        min = total - sum(nums[:total])
        swaps = min
        for i in range(len(nums) - total - 1):
            swaps = swaps - nums[i + total] + nums[i]
            if swaps < min:
                min = swaps
        return min
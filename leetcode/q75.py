# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

def sortColors(nums: list[int]) -> None:
        

        # BUBBLE SORT


        # n=len(nums)
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        # return nums




        # BUCKET OR COUNTING SORT



        # count = [0]*3

        # while len(nums)>0:
        #     x = nums.pop(0)
        #     count[x] +=1
        # for i in range(3):
        #     while count[i]>0:
        #         nums.append(i)
        #         count[i] -= 1



        # SELECTION SORT

        

        l , i , r = 0 , 0 , len(nums)-1

        while i<=r:
            if nums[i] == 0:
                nums[l] , nums[i] = nums[i] , nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[r] , nums[i] = nums[i] , nums[r]
                r -= 1

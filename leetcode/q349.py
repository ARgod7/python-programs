def intersection( nums1: list[int], nums2: list[int]) -> list[int]:
        # return list(set(num for num in nums1 if num in nums2))
        return set(nums1) & set(nums2)
        
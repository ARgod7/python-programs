# MEDIAN OF 2 SORTED ARRAYS



def findMedianSortedArrays(nums1, nums2) -> float:
        left = (len(nums1)+len(nums2)+1)//2
        if len(nums1)>len(nums2):
            nums1 , nums2 = nums2 , nums1
        low , high = 0 , len(nums1)
        while(low<=high):
            mid1 = (low + high)//2
            mid2 = left - mid1
            r1 = nums1[mid1] if mid1<len(nums1) else float("infinity")
            r2 = nums2[mid2] if mid2<len(nums2) else float("infinity")
            l1 = nums1[mid1 - 1] if (mid1-1)>=0 else float("-infinity")
            l2 = nums2[mid2 - 1] if (mid2-1)>=0 else float("-infinity")
            if (l1<=r2) and (l2<=r1):
                if (len(nums1)+len(nums2))%2 == 1:
                    return float(max(l1,l2))
                return float((max(l1,l2)+min(r1,r2))/2)
            elif l1>r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
print(findMedianSortedArrays([1,2],[3,4]))



# shorter version

# return median(sorted(nums1+nums2))
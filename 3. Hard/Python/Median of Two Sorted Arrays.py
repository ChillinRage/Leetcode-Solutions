def findMedianSortedArrays(nums1, nums2):
    array = sorted(nums1 + nums2)
    
    if len(array) % 2 == 0:
        return (array[len(array)//2] + array[len(array)//2 -1])/2
    
    return array[len(array)//2]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c=nums1.count(0)-m
        while 0 in nums1 and n:
            nums1.remove(0)
            n-=1
        nums1+=nums2
        nums1.sort()
        
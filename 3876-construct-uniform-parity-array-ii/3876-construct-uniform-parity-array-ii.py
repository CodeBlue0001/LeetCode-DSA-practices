class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        if min(nums1)%2!=0:
            return True
        even=[]
        for i in nums1:
            if i%2==0:
                even+=[i]
        return len(even)==len(nums1)
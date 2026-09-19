class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # target TC O(n) SC O(1)
        unique={}
        for n in nums:
            if n not in unique:
                unique[n]=1
            else:
                unique[n]+=1
        for n,c in unique.items():
            if c==1:
                return n

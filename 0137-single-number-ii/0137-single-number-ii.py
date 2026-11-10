class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one=0
        two=0
        for n in nums:
            one=(one^n)& ~two
            two=(two^n)& ~one
            print(one,two)
        return one
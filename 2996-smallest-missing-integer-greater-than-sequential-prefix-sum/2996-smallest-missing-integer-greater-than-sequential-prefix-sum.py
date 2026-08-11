class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sn=nums
        print(sn)
        prefix=sn[0]
        for i in range(1,len(sn)):
            
            if sn[i]==sn[i-1]+1:
                prefix+=sn[i]
                print(prefix,sn[i])
            else:
                break
        while True:
            if prefix in sn:
                prefix+=1
            else:
                return prefix
        
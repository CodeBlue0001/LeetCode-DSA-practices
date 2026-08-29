class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        fst=0
        lst=len(nums)-1
        output=[]
        # maps={}
        nums.sort()
        print(nums)
        for i in range(lst-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            n1=nums[i]
            j=i+1
            k=lst
            while j<k:
                if n1+nums[j]+nums[k]>0:
                    k-=1  
                elif n1+nums[j]+nums[k]<0:
                    j+=1
                elif n1+nums[j]+nums[k]==0:
                    output+=[[n1,nums[j],nums[k]]]
                    j+=1
                    k-=1
                    while nums[k]==nums[k+1] and j<k:
                        k-=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                
               
       
        print(output)
        return output
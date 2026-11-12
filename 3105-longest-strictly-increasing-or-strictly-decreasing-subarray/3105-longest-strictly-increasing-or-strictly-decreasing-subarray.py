class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # incrs=[]
        linc=0
        dinc=0
        # decrs=[]
        i=0
        while i<len(nums):
            n=nums[i]
            temp1=[n]

            for j in range(i+1,len(nums)):
                if n<nums[j]:
                    temp1+=[nums[j]]
                    n=nums[j]
                    i=j
                else:
                    break
            
            if linc<len(temp1):
                linc=len(temp1) 
            i+=1
        # print(incrs)
        i=0
        while i<len(nums):
            n=nums[i]
            temp2=[n]
            for j in range(i+1,len(nums)):
                if n>nums[j]:
                    temp2+=[nums[j]]
                    n=nums[j]
                    i=j
                else:
                    break
            # if len(temp2)>1:
                # decrs+=[temp2]
            if len(temp2)>dinc:
                dinc=len(temp2)
            i+=1
        # print(decrs)
        if linc==0 and dinc==0:
            return 1
        return max(linc,dinc)
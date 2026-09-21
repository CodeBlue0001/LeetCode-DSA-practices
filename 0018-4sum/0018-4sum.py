class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        left=0
        right=len(nums)-1
        result=[]
        nums.sort()
        for i in range(right-2):
            # skip duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,right-1):
                n1=nums[i]
                n2=nums[j]
                # skip duplicates
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=right

                while k<l:
                    total =(n1+n2)+nums[k]+nums[l]
                    # print(n1,n2,nums[k],nums[l],total)
                    if total >target:
                        l-=1
                    elif total<target:
                        k+=1
                    else:
                        result+=[[n1,n2,nums[k],nums[l]]]
                        
                        while  k<l and nums[k]==nums[k+1] :
                            k+=1
                        while  k<l and nums[l]==nums[l-1] :
                            l-=1
                        k+=1
                        l-=1
                        
                        
        print(result)
        return result

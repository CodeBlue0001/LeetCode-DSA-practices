class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        for n1 in arr1:
            # item=n1+d
            for n2 in arr2:
                if abs(n1-n2)<=d:
                    count+=1
                    break
        return len(arr1)-count
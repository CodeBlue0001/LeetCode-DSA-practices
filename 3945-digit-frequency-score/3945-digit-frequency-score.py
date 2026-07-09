class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq={}
        for i in str(n):
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        ans=0
        for key,value in freq.items():
            ans+=(int(key)*value)
            # print(key,value)
        return ans
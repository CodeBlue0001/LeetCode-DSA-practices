class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # o(n2) ham\ve to find optimized way
        # temp=list(set(arr))
        # temp.sort()
        # ans=[]
        # for num in arr:
        #     ans+=[temp.index(num)+1]
        # return ans

        #using hash map
        unq_val=sorted(set(arr))
        # creating an hash map for rank and the number
        rank_map={num:i+1 for i,num in enumerate(unq_val)}
        # creating the rank list
        ans=[rank_map[val] for val in arr]
        return ans

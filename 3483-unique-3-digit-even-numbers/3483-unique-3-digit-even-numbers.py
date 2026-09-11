class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_evens=set()
        for d1,d2,d3 in permutations(digits,3):
            if d1!=0 and d3%2==0:
                unique_evens.add(d1*100+d2*10+d3)
        return len(unique_evens)
class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        r=""
        len_=len(lst)-1
        for word in lst[::-1]:
            r+=word

            if len_:
                r+=" "
                len_-=1
        return r
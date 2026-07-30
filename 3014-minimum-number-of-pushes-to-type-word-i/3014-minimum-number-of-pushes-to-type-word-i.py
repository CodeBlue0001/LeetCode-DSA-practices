class Solution:
    def minimumPushes(self, word: str) -> int:
        key_map=list(set(word))
        
        len_map=len(list(key_map))
        result=0
        
        word_map={}
        for i,char in enumerate(word):
            if char in word_map:
                word_map[char]+=1
            else:
                word_map[char]=1
       
        for i, f in enumerate(word_map):
            result += word_map[f] * (i // 8 + 1)
        return result
        
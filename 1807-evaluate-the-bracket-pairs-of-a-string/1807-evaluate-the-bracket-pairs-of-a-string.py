class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        _map={}
        for pair in knowledge:
            _map[pair[0]]=pair[1]
        # print(_map)
        ans=""
        i=0
        # check for bracket and after that search for the word and replace with the value
        while i <len(s):
            char=s[i]
            key=""
            if char=='(':
                j=i+1
                while s[j]!=')':
                    key+=s[j]
                    j+=1
                # replace the key
                # print('key',key)
                if key in _map:
                    # print(ans,_map[key])
                    ans+=_map[key]
                else:
                    ans+='?'
                i=j
                # print(i)
            elif s[i]==')':
                # ans+=" "
                i+=1
            else:
                ans+=s[i]
                i+=1
        # print(ans)
        return ans
            
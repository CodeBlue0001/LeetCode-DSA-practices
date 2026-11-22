class Solution:
    def checkString(self, s: str) -> bool:
        flag=False
        for char in s:
            if char=='b':
                flag=True
            if flag and char=="a":
                return False
        return True
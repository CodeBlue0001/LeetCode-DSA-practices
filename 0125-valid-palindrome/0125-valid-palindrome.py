class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # removing the spaces
        # cleaned=s.replace(" ", "")
        # cleaned=cleaned.replace(",","")
        # cleaned=cleaned.replace(":","")
        # cleaned=cleaned.replace(".","")
        # cleaned=cleaned.replace("$","")
        # cleaned=cleaned.replace("/","")
        # cleaned=cleaned.replace("\\","")
        # cleaned=cleaned.replace("@","")
        # cleaned=cleaned.replace("%","")
        # cleaned=cleaned.replace("#","")
        # cleaned=cleaned.replace(")","")
        # cleaned=cleaned.replace("(","")
        # cleaned=cleaned.replace("&","")
        # cleaned=cleaned.replace("!","")
        # cleaned=cleaned.replace("_","")
        # cleaned=cleaned.replace("[","")
        # cleaned=cleaned.replace("]","")
        # cleaned=cleaned.replace("{","")
        # cleaned=cleaned.replace("}","")
        # cleaned=cleaned.replace("'","")
        # cleaned=cleaned.replace('"',"")
        lst="!@#$%^&*()_\"+-=\|{][}'?/;:.,<>*+ ~`"
        for i in lst:
            s=s.replace(i,"")
        s=s.lower()
        # print(cleaned)
        if s==s[::-1]:
            return True
        else:
            return False

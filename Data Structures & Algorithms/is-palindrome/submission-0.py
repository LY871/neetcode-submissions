import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=re.sub(r'[^A-Za-z0-9]','',s) 
        res=res.lower()
        if res==res[::-1]:
            return True
        else:
            return False        
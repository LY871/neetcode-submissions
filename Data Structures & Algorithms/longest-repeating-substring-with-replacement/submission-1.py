class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        h={}
        max_char=0
        longest=0
        while r<len(s):
            if s[r] in h:
                h[s[r]]+=1
            else:
                h[s[r]]=1
            max_char=max(max_char,h[s[r]])
            if r-l+1-max_char>k:
                h[s[l]]-=1
                l+=1
            longest=max(r-l+1,longest)
            r+=1
        return longest

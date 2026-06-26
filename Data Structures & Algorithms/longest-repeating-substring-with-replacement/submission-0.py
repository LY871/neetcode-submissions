class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo={}
        l=0
        r=0
        max_freq=0
        ret=0
        while r<len(s):
            if s[r] in memo:
                memo[s[r]]+=1
            else:
                memo[s[r]]=1
            max_freq=max(max_freq,memo[s[r]])
            if r-l+1-max_freq>k:
                memo[s[l]]-=1
                l+=1
            ret=max(r-l+1,ret)
            r+=1
        return ret
            



            


                
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table={}
        i=0
        r=0
        max_length=0
        while r<len(s):
            if s[r] in hash_table and hash_table[s[r]]>=i:
                i=hash_table[s[r]]+1
                hash_table[s[r]]=r
            else:
                hash_table[s[r]]=r
            max_length=max(max_length,r-i+1)
            r+=1
        return max_length

            


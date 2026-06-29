class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h={}
        l=0
        longest=1
        if not s:
            return 0
        for i in range(len(s)):
            if s[i] in h and h[s[i]]>=l:
                l=h[s[i]]+1
                h[s[i]]=i
            else:
                h[s[i]]=i
            longest=max(longest,i-l+1)
        return longest
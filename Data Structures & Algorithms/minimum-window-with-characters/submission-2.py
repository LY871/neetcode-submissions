class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        list1=[0]*128
        list2window=[0]*128
        for i in t:
            list1[ord(i)-ord('A')]+=1
        l=0
        r=0
        valid=0
        long=''
        while r<len(s):
            r1=ord(s[r])-ord('A')
            list2window[r1]+=1
            if list2window[r1]<=list1[r1]:
                valid+=1
            while valid==len(t):
                l1=ord(s[l])-ord('A')
                if long=='' or len(long)>len(s[l:r+1]):
                    long=s[l:r+1]
                list2window[l1]-=1
                if list2window[l1]<list1[l1]:
                    valid-=1
                l+=1
            r+=1
        return long






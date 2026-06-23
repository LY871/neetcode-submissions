class Solution:
    #  5#hello5#world
    def encode(self, strs: List[str]) -> str:
        ret=''
        for i in strs:
            length=len(i)
            ret+=str(length)+"#"+i
        return ret
    def decode(self, s: str) -> List[str]:
        i=0
        ret=[]
        curr_len=''
        word=''
        while i<len(s):
            print(curr_len)
            if s[i].isnumeric():
                curr_len+=s[i]
                i+=1
            elif s[i]=="#":
                i+=1
                actual_len=int(curr_len)
                curr_len=''
                word=''
                while actual_len>0 and i<len(s):
                    word+=s[i]
                    actual_len-=1
                    i+=1
                ret.append(word)
        return ret
                
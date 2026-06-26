class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=[]
        hold=0
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                if digits[i]>=9:
                    hold+=1
                    s.append((0))
                else:
                    s.append(digits[i]+1)
            elif digits[i]>=9 and hold!=0:
                s.append(0)
            elif digits[i]<9 and hold!=0:
                s+=[digits[i]+hold]
                hold=0
            else:
                s.append((digits[i]))
        if hold!=0:
            s.append(hold)
        return s[::-1]




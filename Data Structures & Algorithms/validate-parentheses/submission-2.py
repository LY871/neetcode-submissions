class Solution:
    def isValid(self, s: str) -> bool:
        right=']})'
        left='[{('
        stack=[]
        if len(s)==1:
            return False
        if len(s)==0:
            return True
        for i in s:
            if i in left:
                stack.append(i)
            elif i in right:
                if stack:
                    x=stack.pop()
                    if x in left and left.index(x)!=right.index(i):
                        return False
                else: return False
        if not stack:
            return True
        else:
            return False

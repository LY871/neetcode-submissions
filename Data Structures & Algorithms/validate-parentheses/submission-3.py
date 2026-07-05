class Solution:
    def isValid(self, s: str) -> bool:
        l='{[('
        r='}])'
        stack=[]
        for i in s:
            if i in l:
                stack.append(i)
            elif i in r:
                if stack:
                    x=stack.pop()
                    if l.index(x)!=r.index(i):
                        return False
                else:
                    return False
        if stack:
            return False
        return True


                
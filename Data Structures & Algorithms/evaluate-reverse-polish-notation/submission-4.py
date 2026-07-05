class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in "+-*/":
                x=stack.pop()
                y=stack.pop()
                if i=="+":
                    stack.append(x+y)
                elif i=="-":
                    stack.append(y-x)
                elif i=="*":
                    stack.append(x*y)
                else:
                    stack.append(int(y/x))
            else:
                stack.append(int(i))
        return stack[-1]
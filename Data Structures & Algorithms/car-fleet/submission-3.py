class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed))
        stack=[]
        for i in range(len(cars)-1,-1,-1):
            p,s=cars[i]
            time=(target-p)/s
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)
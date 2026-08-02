class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]
        rightmax=[0]*len(height)
        rightmax[-1] = height[-1]
        water=0
        leftmax[0] = height[0]
        for i in range(1,len(height)):
            leftmax.append(max(height[i],leftmax[i-1]))
        for i in range(len(height)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])
        for i in range(len(height)):
            water+=min(leftmax[i],rightmax[i])-height[i]
        return water

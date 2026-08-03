class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum_rect=0
        for i in range(len(heights)):
            right=i+1
            left=i-1
            while right<len(heights) and heights[right]>=heights[i]:
                right+=1
            while left>=0 and heights[left]>=heights[i]:
                left-=1
            width=right-left-1
            maximum_rect=max(maximum_rect,width*heights[i])
        return maximum_rect


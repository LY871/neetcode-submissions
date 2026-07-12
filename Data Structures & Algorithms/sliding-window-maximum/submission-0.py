class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi=[]
        i=0
        r=k
        while len(nums)>=r:
            maxi.append(max(nums[i:r]))
            i+=1
            r+=1
        return maxi
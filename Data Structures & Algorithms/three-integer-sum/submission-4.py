class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        right=len(nums)-1
        ret=[]
        for i in range(len(nums)):
            right=len(nums)-1
            left=i+1
            while left<right:
                sum_both=nums[left]+nums[right]
                if sum_both+nums[i]>0:
                    right-=1
                elif sum_both+nums[i]<0:
                    left+=1
                elif sum_both+nums[i]==0:
                    q=[nums[i],nums[left],nums[right]]
                    left+=1
                    right-=1
                    q.sort()
                    if q not in ret:
                        ret.append(q)
        return ret

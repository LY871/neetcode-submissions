class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        for i in range(len(nums)):
            if i==0:
                left.append(nums[i])
            else:
                left.append(left[i-1]*nums[i])
        right=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right[i]=nums[i]
            else:
                right[i]=right[i+1]*nums[i]
        ret=[]
        for i in range(len(nums)):
            if i==len(nums)-1:
                ret.append(left[i-1])
            elif i==0:
                ret.append(right[i+1])
            else:
                ret.append(right[i+1]*left[i-1])
        return ret

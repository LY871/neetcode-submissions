class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=list(set(nums))
        nums_set.sort()
        print(nums_set)
        maximum_len=1
        count=1
        if not len(nums):
            return 0
        for i in range(len(nums_set)-1):
            if nums_set[i]+1==nums_set[i+1]:
                count+=1
                maximum_len=max(count,maximum_len)
            else:
                count=1

        return maximum_len
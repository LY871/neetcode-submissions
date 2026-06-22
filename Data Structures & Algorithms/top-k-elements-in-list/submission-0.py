class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        unique=set(nums)
        for i in unique:
            h[i]=0
        for i in nums:
            h[i]+=1
        ret=dict(sorted(h.items(), key=lambda x:x[1], reverse=True))
        return list(ret)[:k]


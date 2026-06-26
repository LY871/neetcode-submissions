class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s=[]
        res=[]
        def backtrack():
            if len(s)==len(nums):
                res.append(s[:])
                return
            for i in nums:
                if i not in s:
                    s.append(i)
                    backtrack()
                    s.pop()
        backtrack()
        return res

                
            
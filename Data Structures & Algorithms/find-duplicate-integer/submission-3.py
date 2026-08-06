class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_dic={}
        for i in nums:
            if i in hash_dic:
                return i
            else:
                hash_dic[i]=1

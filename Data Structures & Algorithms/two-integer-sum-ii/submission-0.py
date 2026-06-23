class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            s=target-numbers[i]
            if s in seen:
                k=[i+1,seen[s]+1]
                k.sort()
                return k
            else:
                seen[numbers[i]]=i
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        unique=set(strs)
        ret=[]
        for i in unique:
            h["".join(sorted(list(i)))]=[]
        for i in strs:
            if "".join(sorted(list(i))) in h:
                h["".join(sorted(list(i)))].append(i)
        for i in h:
            ret.append(h[i])
        return ret
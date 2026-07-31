class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        min_pile=r
        while l<=r:
            mid=(l+r)//2
            k=sum([math.ceil(i/mid) for i in piles])
            if k<=h and mid<min_pile:
                min_pile=mid
                r=mid-1
            elif k>h:
                l=mid+1
            else:
                r=mid-1
        return min_pile
            
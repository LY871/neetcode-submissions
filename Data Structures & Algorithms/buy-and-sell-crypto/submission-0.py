class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice=0
        for i in range(len(prices)-1):
            a=max(prices[i+1:len(prices)])-prices[i]
            if a>maxprice:
                maxprice=a
        return maxprice




#https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List


class Solution:
    def maxProfit(self,prices:List[int])->int:
        profit=0
        minBuy=prices[0]
        for i in range (len(prices)):
            currValue=prices[i]
            minBuy=min(minBuy,currValue)
            profit=max(profit,currValue-minBuy)
        return profit

if __name__=="__main__":
    t=Solution()
    print(t.maxProfit(prices = [7,1,5,3,6,4]))



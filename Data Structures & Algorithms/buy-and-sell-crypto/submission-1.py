class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        l, r = 0, 1
        while l < r and r < len(prices):
            if prices[l] < prices[r]:
                best = max(prices[r] - prices[l], best)
            else:
                l=r

            r+=1

        return best
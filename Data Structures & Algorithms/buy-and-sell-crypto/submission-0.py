class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        for i, first in enumerate(prices):
            for j in range(i+1, len(prices)):
                if prices[j] - first > best:
                    best = prices[j] - first

        return best
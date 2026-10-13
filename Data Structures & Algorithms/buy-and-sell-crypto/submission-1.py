class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maxprof = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                prof = prices[j] - prices[i]
                maxprof = max(maxprof, prof)
            else:
                i = j
            j += 1
                     
        return maxprof
        
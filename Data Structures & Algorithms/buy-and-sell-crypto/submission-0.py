class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        i = 0
        j = l-1
        maxprof = 0
        while (i < j):
            while (i<j):
                p1 = prices[i]
                p2 = prices[j]
                prof = p2 - p1
                maxprof = max(prof, maxprof)
                j -= 1

            i += 1
            j = l-1
        return maxprof
        
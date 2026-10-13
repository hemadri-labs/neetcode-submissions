class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # (i-j) * min (h[i], h[j])
        i = 0
        j = len(heights)-1
        maxvol = 0
        while (i<j):
            p1 = heights[i]
            p2 = heights[j]
            vol = (j-i) * min(p1, p2)
            maxvol = max(maxvol, vol)
            if p1 > p2:
                j -= 1
            else:
                i += 1
        
        return maxvol
            
        

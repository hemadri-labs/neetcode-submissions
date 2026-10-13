class Solution:
    def maxArea(self, h: List[int]) -> int:
        lidx = 0
        ridx = len(h) - 1
        mx = 0
        while (lidx < ridx):
            if (h[lidx] < h[ridx]):
                mx = max(mx, ((ridx-lidx)*h[lidx]))
                lidx+=1
            else:
                mx = max(mx, ((ridx-lidx)*h[ridx]))
                ridx-=1
        return mx

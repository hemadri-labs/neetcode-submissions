class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        arr = []
        for i in range(0, n+1):
            k=i
            while (k):
                k = k & (k-1)
                count+=1
            arr.insert(i, count)
            count = 0
        return arr
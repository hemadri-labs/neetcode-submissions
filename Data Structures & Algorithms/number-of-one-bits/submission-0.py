class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        '''
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count;
        '''
        while n:
            n = n & (n-1)
            count += 1
        return count
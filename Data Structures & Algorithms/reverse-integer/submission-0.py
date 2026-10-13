class Solution:
    def reverse(self, n: int) -> int:
        k = 0
        res = 0
        neg = 1
        int_min = (0x80000000) * -1
        int_max = 0x7fffffff
        if n < 0:
            n = n * -1
            neg = -1
        
        while (n != 0):
            k = (n % 10)
            n = (n // 10)
            res = (res * 10) + k
        
        res = (neg * res)
        if int_min <= res <= int_max:
            return int(res)
        else:
            return 0
        
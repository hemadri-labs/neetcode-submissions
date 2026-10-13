class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        01010101 0x55555555
        10101010 0xaaaaaaaa
        10001011 => 11010001

        '''
        print(f"num:{n} - {bin(n)}")
        n = (n >> 16) | (n << 16) & 0xffffffff
        n = ((n & 0xff00ff00) >> 8) | (((n) & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | (((n) & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | (((n) & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        print(f"num:{n} - {bin(n)}")
        return n & 0xffffffff


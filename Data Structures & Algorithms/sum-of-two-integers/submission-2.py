class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        max_int = 0x7fffffff
        sum = (a ^ b) & mask
        carry = (a & b) << 1

        while (carry !=0):
            next_sum = (sum ^ carry) & mask
            next_carry = (sum & carry) << 1
            sum = next_sum
            carry = next_carry
        
        if sum <= max_int:
            return sum
        else:
            return ~(sum ^ mask)

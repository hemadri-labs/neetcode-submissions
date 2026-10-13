class Solution:
    def getSum(self, a: int, b: int) -> int:
        psum = (a ^ b) & 0xffffffff
        carry = (a & b) << 1

        while (carry != 0):
            new_psum = (psum ^ carry) & 0xffffffff
            new_carry = (psum & carry) << 1
            psum = new_psum
            carry = new_carry
        
        if psum <= 0x7ffffff:
            return psum
        else:
            return ~(psum ^ 0xffffffff)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left < right:
            print (f"left {left} right {right} shifts {shifts}")
            left = left >> 1
            right = right >> 1
            shifts +=1
            print (f"left {left} right {right} shifts {shifts}")
        return left << shifts
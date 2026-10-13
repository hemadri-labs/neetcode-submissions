class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        if not nums:
            return xor
        for n in nums:
            xor = n ^ xor
        return xor
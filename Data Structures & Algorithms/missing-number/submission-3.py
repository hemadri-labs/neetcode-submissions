class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        xor = 0
        for n in range(l+1):
            xor = xor ^ n
        for k in nums:
            xor = xor ^ k

        return xor
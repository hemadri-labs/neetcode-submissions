class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in range(len(nums)+1):
            xor = xor ^ n
        for k in nums:
            xor = xor ^ k
        
        return (xor)
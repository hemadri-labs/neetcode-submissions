class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nl = len(nums)
        al = 2*nl
        ans = [0] * al
        for r in range(nl):
            ans[r] = ans[r+nl] = nums[r]
        print(f"ans: {ans}")
        return ans

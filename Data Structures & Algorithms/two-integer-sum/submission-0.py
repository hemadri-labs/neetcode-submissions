class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx = {}
        for i,v in enumerate(nums):
            indx[v] = i
        for i,v in enumerate(nums):
            diff = target - v
            if diff in indx and indx[diff] != i:
                return [i, indx[diff]]
        return []

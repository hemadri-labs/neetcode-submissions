class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  # To store the final result

        stack = [([], 0, 0)]

        while stack:
            path, total, start = stack.pop()
            if total == target:
                res.append(path)
                continue
            for i in range(start, len(nums)):
                if nums[i] + total <= target:
                    stack.append((path + [nums[i]], total+nums[i], i))
        return res
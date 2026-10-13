class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums) - 1
        res = []
        print(f"{nums}")
        for i in range(len(nums)-2):
            left = i+1
            right = l
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    while ((left < right ) and (nums[left] == nums[left+1])):
                        left+=1
                    left+=1
                elif total > 0:
                    while((left < right) and (nums[right] == nums[right-1])):
                        right-=1
                    right-=1
                elif total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left+=1
                    right-=1
                
        return res
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        def bin_search(nums, l, r) -> int:

            while (l<=r):
                m = l + (r-l)//2
                if nums[m] == target:
                    return m    
                #left array is sorted
                if nums[l] <= nums[m]:
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    #right array is sorted
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
            return -1

        v = bin_search(nums, l , r)
        return v


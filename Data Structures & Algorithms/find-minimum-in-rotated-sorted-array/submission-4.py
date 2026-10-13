class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        def bin_search(nums, l, r) -> int:
            while (l<=r):
                m = l + (r-l)//2
                if nums[l] > nums[m]:
                    if nums[m] < nums[r]:
                        r = m
                    else:
                        l = m
                elif nums[m] >= nums[l] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            return nums[l]
        l = 0
        r = len(nums) - 1
        v = bin_search(nums, l, r)
        return v
        '''
        l = 0
        r = len(nums) - 1
        while (l < r):
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]




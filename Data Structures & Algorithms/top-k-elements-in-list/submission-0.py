class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        buckets = [[] for _ in range(len(nums)+1)]

        for n,freq in count.items():
            buckets[freq].append(n)
        
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]

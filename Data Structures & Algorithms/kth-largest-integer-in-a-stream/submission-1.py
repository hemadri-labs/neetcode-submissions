class KthLargest:
    '''
    always keep only largest K elements in minHeap and return top of the minheap, which is the kth largest number 
    '''
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k or val > self.minheap[0]:
            heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]
        

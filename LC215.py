class Solution(object):
    def findKthLargest(self, nums, k):
      import heapq
      heap = [-x for x in nums]

      heapq.heapify(heap)
      for _ in range(k-1):
        heapq.heappop(heap)
      
      return -heapq.heappop(heap)

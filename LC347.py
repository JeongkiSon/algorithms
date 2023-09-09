class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        dd = {}
        for v in nums:
            dd[v] = dd.get(v, 0) + 1
        
        # print(list(dd.items()))
        ss = list(dd.items())
        ss.sort(reverse=True, key = lambda x: x[1])
        print(ss)
        ans = []

        for idx in range(k):
            ans.append(ss[idx][0])
        
        return ans
        '''
        # O(nlogn)

        # Using Heap
        import heapq
        dd = {}
        for v in nums:
            dd[v] = dd.get(v, 0) + 1
        
        ll = []
        for n, c in dd.items():
            ll.append((-c, n)) # change the order!! and heapq is minheap  "-c"
        
        heapq.heapify(ll)
        # print(ll) # [(1, 3), (2, 2), (3, 1)]
    
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(ll)[1])
        
        return ans


        

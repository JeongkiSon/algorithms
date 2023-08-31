class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        
        for h in range(papers,0,-1):
            flag = True
            cnt = papers
            for i in range(papers):
                if citations[i] < h:
                    cnt = cnt -1
                    if cnt < h:
                        flag = False
                        break
            if flag == True:
                return h
        return 0
                




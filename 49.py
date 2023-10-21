class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashes = []
        for word in strs:
            hash = {}
            for k in word:
                hash[k] = hash.get(k, 0) + 1
            if hash in hashes:
                idx = hashes.index(hash)
                res[idx].append(word)
            else:
                res.append([word])
                hashes.append(hash)
        
        return res
      

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for s in strs:
          if len(s) < min_len:
            min_len = len(s)
        strlist = strs
        res = ""
        for i in range(min_len):
          check = set()
          for s in strlist:
            if s == "":
              return res
            else:
              check.add(s[0])
          if len(check) == 1:
            res += strlist[0][0]
          else:
            return res
          strlist = [ss[i+1:] for ss in strs]
          print(strs)
        
        return res

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'[' : ']', '{' : '}', '(' : ')'}
        open = ['(', '{', '[']
        stack = []

        for par in s:
            if par in open:
                stack.append(par)
            else:
                if not stack:
                    return False
                else:
                    temp = stack.pop()
                    if pair[temp] != par:
                        return False

        if stack: return False
        else: return True
        

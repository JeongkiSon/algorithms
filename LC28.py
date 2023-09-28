class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        h_len = len(haystack)
        for i, letter in enumerate(haystack):
            if letter == needle[0] and h_len - i >= n_len:
                if haystack[i: i + n_len] == needle:
                    return i
        return -1

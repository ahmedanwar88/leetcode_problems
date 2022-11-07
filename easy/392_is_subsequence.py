#Reference https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/is-subsequence.py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        i = 0
        for c in t:
            if s[i] == c:
                i+=1
            if i == len(s):
                break
        return i == len(s)
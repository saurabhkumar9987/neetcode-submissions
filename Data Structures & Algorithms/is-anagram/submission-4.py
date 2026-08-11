class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)

        if ''.join(sortedS)==''.join(sortedT): 
            return True 
        else: 
            return False
        
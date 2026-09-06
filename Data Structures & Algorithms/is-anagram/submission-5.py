class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ''.join(sorted(s)) == ''.join(sorted(t)): 
            return True 
        else: 
            return False






        # sortedS = sorted(s)
        # sortedT = sorted(t)

        # if ''.join(sortedS)==''.join(sortedT): 
        #     return True 
        # else: 
        #     return False
        
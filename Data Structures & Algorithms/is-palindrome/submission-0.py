class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = list(s.lower())
        output = [] 
        for i in sentence: 
            if i.isalnum(): 
                output.append(i)
        print(output)
        if ''.join(output[::-1]) == ''.join(output): 
            return True 
        else: 
            return False
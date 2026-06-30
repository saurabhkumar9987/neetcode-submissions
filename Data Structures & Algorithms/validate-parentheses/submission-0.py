class Solution:
    def isValid(self, s: str) -> bool:
        maps = { ')':'(', 
                 '}':'{',
                 ']':'['
        }
        ## list implementation of stack 
        stack = []
        for i in s: 
            if i in maps: 
                if stack and stack[-1]==maps[i]: 
                    stack.pop() 
                else:
                    return False 
            else: 
                stack.append(i)

        if stack: 
            return False 
        else: 
            return True



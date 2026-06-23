class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ### compare length of array and length of set 
        # if len(nums)==len(set(nums)): 
        #     return False 
        # else: 
        #     return True 

        ### build a dictionary 
        if len(nums) > 1: 
            freq = {} 
            for i in nums: 
                if i in freq: 
                    freq[i] += 1 
                else: 
                    freq[i] = 1 
            
            max_value = max(freq.values())
            if max_value > 1: 
                return True 
            else: 
                return False
        else: 
            return False
        
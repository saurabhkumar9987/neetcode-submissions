class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {} 
        max_freq = len(nums)/2 
        for n in nums: 
            if n in freq: 
                freq[n] += 1 
            else: 
                freq[n] = 1 

        
        for k,v in freq.items(): 
            if v >= max_freq: 
                return k 



        
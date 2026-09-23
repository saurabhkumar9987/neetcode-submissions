class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums_freq = {} 
        for i in nums: 
            if i in nums_freq: 
                nums_freq[i] += 1 
            else: 
                nums_freq[i] = 1 

        largest = -1

        for k,v in nums_freq.items(): 
            if v==1 and k > largest: 
                largest = k
        

        return largest 
        

        
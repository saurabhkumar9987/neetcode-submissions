class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {} 
        

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i],0)

        
        top_k_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]
        top_k_items =  dict(top_k_items) 
        res = []
        for i,j in top_k_items.items(): 
            res.append(i)
        
        return res

        
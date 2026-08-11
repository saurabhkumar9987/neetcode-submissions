class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {} 
        for i in nums:
            if i in nums_map: 
                nums_map[i] += 1 
            else: 
                nums_map[i] = 1 
        
        output = sorted(nums_map.items(),key=lambda x:x[1], reverse=True)
        final = [] 
        for i in range(k):
            final.append(output[i][0])

        return final 
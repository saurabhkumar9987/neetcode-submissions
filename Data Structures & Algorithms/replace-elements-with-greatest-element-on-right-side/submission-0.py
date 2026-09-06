class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = 0 
        
        for r in range(l+1,len(arr)): 
            largest = max(arr[r:]) 
            arr[l] = largest
            l += 1 
        arr[-1] = -1 

        return arr


        
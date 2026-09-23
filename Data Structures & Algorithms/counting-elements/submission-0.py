class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnt = 0 
        for i in range(len(arr)): 
            if arr[i] + 1 in arr: 
                cnt +=1 

        return cnt 
        
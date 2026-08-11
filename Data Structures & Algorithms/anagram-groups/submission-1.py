import collections 
from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)
        for i in strs: 
            strs_map[''.join(sorted(i))].append(i)
       
        return list(strs_map.values())

        
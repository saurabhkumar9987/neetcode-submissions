class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strs: 
            sortedS = ''.join(sorted(s))
            freq[sortedS].append(s)
        
        return list(freq.values())
        
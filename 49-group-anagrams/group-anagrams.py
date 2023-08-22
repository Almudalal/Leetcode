class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        
        for i in strs:
            sortStr = ''.join(sorted(i))
            if sortStr not in hmap:
                hmap[sortStr] = []
            hmap[sortStr].append(i)
        return hmap.values()
            

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numCount = {}
        result = []
        frequency = [[] for i in range(len(nums) + 1)]
    
        for n in nums:
            numCount[n] = 1 + numCount.get(n, 0)
        for n, c in numCount.items():
            frequency[c].append(n)
        
        # iterates down from last index to first by increment of 1.
        for i in range(len(frequency) -1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result

        
        

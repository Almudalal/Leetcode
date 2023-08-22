class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      #Use HashMap 

      hMap = {}

      for i, n in enumerate(nums):
          difference = target - n
          if difference in hMap:
              return [hMap[difference], i]
          hMap[n] = i
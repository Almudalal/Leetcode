class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index1 = 0
        index2 = len(numbers) - 1

        ans = []

        while index1 < index2:
            
            s = numbers[index1] + numbers[index2]
           
            if s == target:
                ans.append(index1 + 1)
                ans.append(index2 + 1)
                return ans
            elif s < target:
                index1 += 1
            else:
                index2 -= 1
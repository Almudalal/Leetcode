class Solution:
    def trap(self, height: List[int]) -> int:

        answer = 0 

        left = 0
        right = len(height) -1 

        leftmax = height[left]
        rightmax = height[right]

        while left < right:
            if leftmax < rightmax:

                left += 1 
                leftmax = max(leftmax, height[left])
                answer += leftmax - height[left]
            
            else:

                right -= 1 
                rightmax = max(rightmax, height[right])
                answer += rightmax - height[right]
        
        return answer
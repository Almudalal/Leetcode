class Solution:
	def productExceptSelf(self, nums: List[int]) ->List[int]:

		n = len(nums)

		postfix = [1] * n
		prefix = [1] * n
		answer = [0] * n

# fills in the left products
		left = 1
		for i in range(1, n):
			left *= nums[i-1]
			postfix[i] = left 
		
# fills in the right products
		right = 1
		for i in range(n-2, -1, -1):
			right *= nums[i+1]
			prefix[i] = right

#multiply both lists of each side together to get the final product
		for i in range(n):
			answer[i] = postfix[i] * prefix[i]
		
		return answer
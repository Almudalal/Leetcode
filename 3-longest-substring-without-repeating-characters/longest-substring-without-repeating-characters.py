class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat = []
        left = 0 
        right = 0
        longestLength = 0

        while right < len(s):
            
            if s[right] not in repeat:
                repeat.append(s[right])
                longestLength = max(longestLength, right - left + 1)
                right += 1
                
            else:
                repeat.remove(s[left])
                left += 1 
        return longestLength
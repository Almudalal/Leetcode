class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hmap = {")":"(", "]":"[" , "}":"{"}

        for i in s:
            if i not in hmap:
                stack.append(i)
                continue
            if not stack or stack[-1] != hmap[i]:
                return False
            stack.pop()
        
        return not stack
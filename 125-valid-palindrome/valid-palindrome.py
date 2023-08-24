class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        remove = ''.join([x for x in s if x.isalpha() or x.isnumeric()]).lower()


        if remove == remove[::-1]:
            return True
        else:
            return False
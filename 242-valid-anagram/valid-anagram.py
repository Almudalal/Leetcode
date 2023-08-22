class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Hashmap Used

        if len(s) != len(t):
            return False

        Smap , Tmap = {} , {}

        for i in range(len(s)):
            Smap[s[i]] = 1 + Smap.get(s[i], 0)
            Tmap[t[i]] = 1 + Tmap.get(t[i], 0)
        for x in Smap:
            if Smap[x] != Tmap.get(x, 0):
                return False
        return True
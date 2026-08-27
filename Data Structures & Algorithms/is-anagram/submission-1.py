class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        d1={}
        d2={}
        for i in range(len(s)):
            char=s[i]
            char_t=t[i]
            d1[char]=d1.get(char,0)+1
            d2[char_t]=d2.get(char_t,0)+1
        if d1==d2:
            return True

        return False
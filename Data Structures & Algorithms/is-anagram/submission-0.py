class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        d1={}
        d2={}
        for i in range(len(s)):
            char=s[i]
            char2=t[i]
            
            d1[char]=d1.get(char,0)+1
 
            d2[char2]=d2.get(char2,0)+1
        
        if d1==d2:
            return True
        else:
            return False
        
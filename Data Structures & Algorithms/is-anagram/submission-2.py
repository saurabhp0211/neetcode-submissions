class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s)!=len(t):
        return False
      
      dict1={}
      dict2={}
      for i in range(len(s)):
        charS=s[i]
        charT=t[i]
        dict1[charS]=dict1.get(charS,0)+1
        dict2[charT]=dict2.get(charT, 0)+1

      if dict1==dict2:
        return True
      
      return False

    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        reqDict={}
        for i in range(len(s1)):
            char=s1[i]
            reqDict[char]=reqDict.get(char, 0)+1

        windowDict={}
        l=0
        for r in range(len(s2)):
            char_r=s2[r]
            windowDict[char_r]=windowDict.get(char_r, 0)+1

            if (r-l+1)>len(s1):
                windowDict[s2[l]]-=1
                
                if windowDict[s2[l]]==0:
                    del windowDict[s2[l]]
                l+=1

            if reqDict==windowDict:
                return True

        return False


            

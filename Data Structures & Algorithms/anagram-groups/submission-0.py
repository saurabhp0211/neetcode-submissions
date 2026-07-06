class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ansDict={}
        for s in strs:
            key="".join(sorted(s))

            if key not in ansDict:
                ansDict[key]=[]
            ansDict[key].append(s)
        return list(ansDict.values())

        
        
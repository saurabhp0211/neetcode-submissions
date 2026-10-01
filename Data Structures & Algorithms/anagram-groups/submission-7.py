class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return []
        seen={}

        
        for s in strs:
            key="".join(sorted(s))
            if key not in seen:
                seen[key]=[]
            seen[key].append(s)
        
        return list(seen.values())

            

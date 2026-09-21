class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        result=[]
        for n in nums:
            seen[n]=seen.get(n,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num, count in seen.items():
            buckets[count].append(num)
        
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result

            
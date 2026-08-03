class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [x for _ in range(2) for x in nums]
        
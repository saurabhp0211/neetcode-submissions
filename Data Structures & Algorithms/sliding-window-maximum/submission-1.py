class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Stores indices
        res = []

        for i, num in enumerate(nums):
            # 1. Remove indices outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

        # 2. Remove indices whose values are smaller than the current element
            while dq and nums[dq[-1]] <= num:
                dq.pop()

        # 3. Add current index
            dq.append(i)

            # 4. Append the current window's max once the window reaches size k
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dq = deque()
        result = []

        for i in range(len(nums)):

            # Remove elements that are outside the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Start adding maximum after first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(nums)

        # Suffix minimum
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Prefix maximum + answer
        max_so_far = nums[0]

        for i in range(n):
            max_so_far = max(max_so_far, nums[i])

            instability = max_so_far - suffix_min[i]

            if instability <= k:
                return i

        return -1
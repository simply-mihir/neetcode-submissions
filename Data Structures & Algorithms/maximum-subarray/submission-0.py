class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, maxs=0,float("-inf")
        for i in nums:
            total+=i
            maxs=max(maxs,total)
            if total<0:
                total=0
        return maxs
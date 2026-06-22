class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for s in range(len(nums)):
            i = nums[s]
            diff=target-i
            n=nums[s+1:]
            if diff in n:
                return [s,n.index(diff)+s+1]

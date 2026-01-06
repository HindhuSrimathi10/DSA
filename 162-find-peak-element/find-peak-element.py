class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_index=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]>nums[max_index]:
                max_index=i
        return max_index       
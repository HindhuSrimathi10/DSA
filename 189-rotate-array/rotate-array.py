class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        i=(n-k)%n
        res=[]
        for _ in range(n):
            res.append(nums[i])
            i=(i+1)%n
        for i in range(n):
            nums[i]=res[i] 
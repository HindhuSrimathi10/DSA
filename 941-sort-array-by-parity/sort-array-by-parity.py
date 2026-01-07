class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # res=[]
        # even=[x for x in nums if x%2==0]
        # odd=[x for x in nums if x%2!=0]
        # res=even+odd
        # return res


# using 2 pointer method
        n=len (nums)
        l=0
        r=n-1

        while l<=r:
            if nums[l]%2!=0:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            else:
                l+=1
        return nums 
        
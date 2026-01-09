class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(permutations(nums))

        # using recursion function by DFS 
        res=[]
        n=len(nums)
        used=[False]*n
        def dfs(path):
            if len(path)==n:
                res.append(path.copy())
                return
            for i in range(n):
                x=nums[i]
                if used[i]==True:
                    continue
                used[i]=True
                dfs(path+[x])
                used[i]=False
        dfs([])
        return res

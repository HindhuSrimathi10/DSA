class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # return list(set(permutations(nums)))
        
        # using recursion 
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
        ans = []
        for li in res:
            ans.append(tuple(li))
        return list(set(ans))
        
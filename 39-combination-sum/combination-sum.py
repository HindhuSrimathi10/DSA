class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)

        def dfs(start,path,total):
            if total ==target:
                res.append(path.copy())
            if total> target:
                return
            for i in range(start,n):
                x=candidates[i]
                dfs(i,path+[x],x+total)
        dfs(0,[],0)
        return res
from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        digits = list(range(1, 10))
        for comb in combinations(digits, k):
            if sum(comb) == n:
                res.append(list(comb))
        return res
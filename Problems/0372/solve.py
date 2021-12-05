class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1
        for e in b:
            ans = pow(ans, 10, MOD) * pow(a, e, MOD) % MOD
        return ans
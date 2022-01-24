class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        mulk = 1
        while n >= mulk:
            count += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk +1, 0), mulk)
            mulk *= 10
        return count
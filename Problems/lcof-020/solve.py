class Solution:
    def isNumber(self, s: str) -> bool:
        return re.compile('^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$').match(s.strip()) is not None
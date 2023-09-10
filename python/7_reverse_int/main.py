class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        x = str(x)
        if x[-1] == 0:
            x = x[:-1]
        elif x[0] == "-":
            is_negative = True
            x = x[1:]
        x = x[::-1]
        if is_negative:
            x = "-" + x
        if x < -(2**31) or x > 2**31:
            return 0
        else:
            return int(x)

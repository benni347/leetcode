class Solution:
    def reverse(self, x: int) -> int:
        # Convert the integer to string and reverse it
        reversed_str = str(x)[::-1]

        # Check if the original number was negative
        if x < 0:
            reversed_str = "-" + reversed_str[:-1]  # Remove the trailing '-'

        # Convert back to integer
        reversed_int = int(reversed_str)

        # Check for 32-bit integer overflow
        if reversed_int < -(2**31) or reversed_int > 2**31 - 1:
            return 0
        return reversed_int

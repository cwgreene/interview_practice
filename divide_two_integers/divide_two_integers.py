class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            sign = 0 - sign 
            dividend = 0 - dividend
        if divisor < 0:
            sign = 0 - sign
            divisor = 0 - divisor
        remainder = dividend
        quotient = 0
        while remainder - divisor >= 0:
            acc = divisor
            count = 1
            while acc + acc < remainder:
                acc = acc + acc
                count = count + count
            quotient += count
            remainder -= acc
        if sign < 0:
            quotient = 0 - quotient
        if quotient > 2147483647:
            return 2147483647
        if quotient < (-2**31):
            return -2**31
        return quotient


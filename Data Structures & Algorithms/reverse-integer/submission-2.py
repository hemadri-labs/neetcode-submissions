class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 0
        max_int = 0x7fffffff
        min_int = -2147483648
        if x < 0:
            sign = 1
            x = -x
            
        while x:
            dig = x % 10
            x = x // 10
            rev = (rev * 10) + dig

        if sign:
            rev = -rev
        print (f"rev={rev}")

        if rev < min_int:
            return 0
        elif rev > max_int:
            return 0
        else:
            return int(rev)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen = len(a)-1
        blen = len(b)-1
        carry = 0
        res = []

        while alen>=0 or blen>=0 or carry>0:
            x = 0 if alen < 0 else int(a[alen])
            y = 0 if blen < 0 else int (b[blen])

            total = x + y + carry
            carry = total // 2
            res.append(total % 2)
            alen-=1
            blen-=1
        res.reverse()
        s = "".join(map(str,res))
        return s
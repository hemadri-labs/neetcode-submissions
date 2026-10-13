class Solution:
    def isHappy(self, n: int) -> bool:
        
        #visit = set()
        visit = []
        while n not in visit:
            visit.append(n)
            n = self.sumofsquares(n)
            if n == 1:
                return True
        return False
        '''
        slow, fast = n, self.sumofsquares(n)
        while (slow != fast):
            slow = self.sumofsquares(slow)
            fast = self.sumofsquares(fast)
            fast = self.sumofsquares(fast)
        if fast == 1:
            return True
        else:
            return False
        '''

    def sumofsquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n %10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output
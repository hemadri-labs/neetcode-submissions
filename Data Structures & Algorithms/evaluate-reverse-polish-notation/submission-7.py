import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        oper = ['+', '-', '*', '/']
        out = 0
        tlen = len(tokens)
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for n in range(tlen):
            if tokens[n] not in oper:
                stack.append(int(tokens[n]))
                #print(f"stack1={stack}")
            elif tokens[n] in oper and stack:
                rval = stack.pop()
                lval = stack.pop()
                out = int(ops[tokens[n]](lval, rval))
                stack.append(out)
                #print(f"stack2={stack}")
        return stack.pop()
        '''
        stack = []
        for c in tokens:
            if c == "+":
                rval = stack.pop()
                lval = stack.pop()
                stack.append(lval + rval)
            elif c == "-":
                rval = stack.pop()
                lval = stack.pop()
                stack.append(lval - rval)
            elif c == "*":
                rval = stack.pop()
                lval = stack.pop()
                stack.append(lval * rval)
            elif c == "/":
                rval = stack.pop()
                lval = stack.pop()
                stack.append(int(lval / rval))
            else:
                stack.append(int(c))
        return stack[0]
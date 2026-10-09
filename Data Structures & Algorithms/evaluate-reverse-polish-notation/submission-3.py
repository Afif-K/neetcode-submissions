class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #operators = ["+", "-", "*", "/"]
        stack = []

        for i in tokens:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(i))
            
        return stack[-1]
               
        


      



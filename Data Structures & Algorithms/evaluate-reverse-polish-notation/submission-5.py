class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))  # Convert to int when pushing to stack
            else:
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)  # Corrected order
                elif token == "*":
                    stack.append(a * b)
                else:
                    # Use integer division and handle division by negative numbers
                    stack.append(int(a / b))  # This truncates towards zero

        return stack.pop()
# Solving time: 33 minutes

# eval_reverse_polish.py
# Evaluate reverse Polish notation expression
# Neetcode. https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150
import math
def evalRPN(tokens: list[str]) -> int:
    """
    Evaluate expression written in reverse Polish notation (https://en.wikipedia.org/wiki/Reverse_Polish_notation)

    Input:
    - `tokens`: list of string tokens with integers and operators `+`, `-`, `*`, `/`

    Output:
    - `int`: result using truncation toward zero for division
    
    Time complexity: O(n), single pass over the tokens
    Space complexity: O(n), stack can hold up to all operands in worst case
    """
    # Guard against empty input
    if tokens:

        # Return single operand when `tokens` has length 1
        if len(tokens) == 1:
            return int(tokens.pop())            
        
        # List operator symbols
        symbols = ["+", "-", "*", "/"]
        # Use `stack` for operands
        stack = []
        for token in tokens:
            if token not in symbols:
                # Push `token` to `stack`
                stack.append(token)
            else: 
                # Construct normal `a OPERATOR b` string
                eval_result = str(stack[-2]) + token + str(stack[-1])
                result = int(eval(eval_result))
                # Pop operands from `stack`
                stack.pop()
                stack.pop()
                # Push result `result` back to `stack`
                stack.append(result)

        # Return last result `result`
        return result
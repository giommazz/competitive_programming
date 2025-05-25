def isValid(s: str) -> bool:
    
    # simple breaking controls
    if len(s) % 2 == 1 or len(set(s)) % 2 == 1:
        return False
    
    bracket_dict = {")": "(", "]": "[", "}": "{"}
    bracket_stack = []

    for bracket in s:
        # if `bracket` is an "opening" bracket '(,' '[', or '{'...
        if bracket not in bracket_dict.keys():
            # ...append it to the stack
            bracket_stack.append(bracket)
        # if it is a "closing" bracket '),' ']', or '}'...
        else:
            # ...check whether the "opening" bracket corresponding to the current "closing" 
            #   `bracket` (i.e., `bracket_dict[bracket]`) is the stack's last element.
            #   Also, `bracket_stack` cannot be empty
            if not bracket_stack or bracket_dict[bracket] != bracket_stack[-1]:
                # if not, return False
                return False
            else:
                bracket_stack.pop()
    # `bracket_stack` must be empty at the end, it means you closed all open brackets
    if bracket_stack:
        return False
    
    return True
""" Topic 8. Valid Parentheses --> LC => 20 """

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            # If opening bracket, push to stack
            if bracket in "([{":
                stack.append(bracket)
            else:
                # For closing bracket, stack cannot be empty
                if len(stack) == 0:
                    return False
                
                # Pop last opening bracket and check if matching
                ch = stack.pop()
                if (bracket == ")" and ch == "(") or \
                   (bracket == "]" and ch == "[") or \
                   (bracket == "}" and ch == "{"):
                    continue
                else:
                    return False
        
        # Check if all opened brackets were closed
        return len(stack) == 0
def isValid(self, s):
        """
        Checks if the input string s containing only brackets is valid.
        A string is valid if all types of brackets are closed in the correct order.
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        # Iterate through each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in '([{':
                stack.append(char)
            # If the character is a closing bracket
            else:
                # If the stack is empty, there is no matching opening bracket
                if not stack:
                    return False
                # Pop the top element from the stack
                top = stack.pop()
                # Check if the popped opening bracket matches the current closing bracket
                if mapping[char] != top:
                    return False
        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0
def isValid(s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        opening = ['(', '[', '{']
        previous = ''
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                if s[i] == ')' and '(' in stack and previous not in ['[', '{'] and stack[-1] == '(':
                    stack.pop(-1)
                elif s[i] == ']' and '[' in stack and previous not in ['(', '{'] and stack[-1] == '[':
                    stack.pop(-1)
                elif s[i] == '}' and '{' in stack and previous not in ['(', '['] and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            previous = s[i]
        if stack == []:
            return True
        return False

print(isValid("[([]])"))


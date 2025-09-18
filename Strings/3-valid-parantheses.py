def solve(inp):
    
    stack = []
    for ch in inp:
        if(ch=='(' or ch=='{' or ch=='['):
                stack.append(ch)
        elif (len(stack)<=0):
                return False #one of the edge cases
        elif (ch==')'):
                if(stack[-1]!='('):
                    return False
                else:
                    stack.pop()
        elif (ch==']'):
                if(stack[-1]!='['):
                    return False
                else:
                    stack.pop()
        elif (ch=='}'):
                if(stack[-1]!='{'):
                    return False
                else:
                    stack.pop()
    if(len(stack)==0):
        return True
    else:
         return False

def main():
    inp = input("Enter the string of parantheses: ")
    flag = solve(inp)
    print(flag)
        
if __name__ == '__main__':
     main()

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
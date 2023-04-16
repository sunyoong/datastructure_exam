from stack import *


def bracket(input_string):
    
    # 스택 준비
    stack = Stack()
    print(input_string)
    # 입력 문자를 하나씩 읽어 왼쪽 괄호를 만나면 스택 저장
    for ch in input_string:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty():
                return False
            else:
                pop_result = stack.pop()
                if (ch==')' and pop_result!='(' or \
                    ch=='}' and pop_result!='{' or \
                    ch==']' and pop_result!='['):
                    return False
                
    return stack.isEmpty()             




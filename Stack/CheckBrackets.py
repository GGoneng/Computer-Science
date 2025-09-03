from StackClass import *

# 스택을 이용한 괄호 검사 알고리즘
def checkBrackets(code):
    stack = ArrayStack(100)

    for ch in code:
        if ch in ["(", "[", "{"]:
            stack.push(ch)
        elif ch in [")", "]", "}"]:
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if ((ch == ")" and left != "(") or 
                   (ch == "]" and left != "[") or 
                   (ch == "}" and left != "{")) :
                   return False
    
    return stack.isEmpty()

if __name__ == "__main__":
    # 괄호 쌍이 맞는 경우
    code1 = "{A[(i+1)]=0;}"
    # 괄호 쌍이 틀린 경우
    code2 = "if ((x<0) && (y<3)"

    print(f"결과 : \n code1 : {checkBrackets(code1)}\n code2 : {checkBrackets(code2)}")
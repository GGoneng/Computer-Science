# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

input1, input2 = map(int, input().split())

L1 = []
L2 = []

if input1 < input2:
    for i in range(1, input1 + 1):
        if ((input1 % i == 0) and (input2 % i == 0)):
            L1.append(i)
        
        if ((input2 * i) % input1 == 0):
            L2.append(i)

    print(max(L1))
    print(min(L2) * input2)

else:
    for i in range(1, input2 + 1):
        if ((input1 % i == 0) and (input2 % i == 0)):
            L1.append(i)

        if ((input1 * i) % input2 == 0):
            L2.append(i)

    print(max(L1))
    print(min(L2) * input1)
    
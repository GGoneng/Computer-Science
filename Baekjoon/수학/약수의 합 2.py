# 문제
# 두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다. x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
# 자연수 N이 주어졌을 때, g(N)을 구해보자.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 g(N)를 출력한다.

input = int(input())

total = 0

def div_calc(input):
    div_list = []

    for i in range(1, int(input ** (1 / 2)) + 1):
        if input % i == 0:
            div_list.append(i)
    
    return div_list

def extend_div(input, div_list):
    extend_list = []

    for div in div_list:
        if div == input ** (1 / 2) :
            extend_list.append(0)
        else:
            extend_list.append(input // div)
    
    return extend_list

for i in range(1, input + 1):
    div_list = div_calc(i)
    extend_list = extend_div(i, div_list)

    div_list.extend(extend_list)

    total += sum(div_list)


print(total)
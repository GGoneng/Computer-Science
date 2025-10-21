# 문제
# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
# 입력이 한번에 들어옴

import sys

for line in sys.stdin:
    n = int(line.strip())

    if n % 2 == 0 or n % 5 == 0:
        continue

    i = "1"
    while True:
        if int(i) % n == 0:
            print(len(i))
            break
        i += "1"

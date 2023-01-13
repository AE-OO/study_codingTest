# 이진 탐색 문제는 입력 데이터의 갯수가 많은 문제가 많다
# 이때 input()을 사용하면 시간 초과 오답이 난다
# 이럴 때는 sys.stdin.readline().rstrip() 을 사용해서 데이터를 입력 받아야 한다

import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)
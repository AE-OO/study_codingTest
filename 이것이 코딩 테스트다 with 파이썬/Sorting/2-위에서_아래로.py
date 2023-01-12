# 몇 개의 수를 입력받을 것인지
n = int(input())

array = []
# 입력 받을 수만큼 반복문을 돌려 리스트에 값을 넣음
for i in range(n):
    array.append(int(input()))

# sorted 함수를 사용해 리스트 내림차순 정렬
array = sorted(array, reverse=True)

# 리스트 형태로 출력되지 않도록 반복문을 돌려 값을 하나씩 출력
for i in array:
    print(i, end=' ')
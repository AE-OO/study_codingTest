# 이진 탐색으로 문제 풀이 - 데이터가 1000만 이하까지니까 순차 탐색보다는 이진 탐색이 효율적
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
# 이진 탐색은 정렬된 리스트에서 사용하기 때문에 값을 받아온 후 정렬을 해 줌
sale_number = list(map(int, input().split()))
sale_number.sort()
m = int(input())
find_number = list(map(int, input().split()))

for i in find_number:
    result = binary_search(sale_number, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 계수 정렬으로 문제 풀이

n = int(input())
# 임의 크기의 리스트 생성
sale_number = [0] * 101

for i in input().split():
    sale_number[int(i)] = 1

print(sale_number)

m = int(input())
find_number = list(map(int, input().split()))

for i in find_number:
    if sale_number[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 집합 자료형으로 문제 풀이

n = int(input())
# set() - 집합 자료형에 추가
sale_number = set(map(int, input().split()))

m = int(input())
find_number = list(map(int, input().split()))

for i in find_number:
    if i in sale_number:
        print('yes', end='')
    else:
        print('no', end='')


# 순차 탐색으로 문제 풀이
# def sequential_search(n, m, find_number, sale_number):
#     for i in range(m):
#         for j in range(n):
#             if find_number[i] == sale_number[j]:
#                 print("yes")
#
# n = int(input())
# sale_number = list(map(int, input().split()))
# m = int(input())
# find_number = list(map(int, input().split()))
#
# sequential_search(n, m, find_number, sale_number)

# 수 정렬하기

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

for i in range(n - 1):
    for j in range(i + 1, n):
        if num[i] > num[j]:
            swap = num[i]
            num[i] = num[j]
            num[j] = swap

for i in range(n):
    print(num[i])
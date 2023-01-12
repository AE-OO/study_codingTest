n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a의 합이 가장 크려면 a의 작은 수와 b의 큰 수를 바꾸면 됨 -> a는 오름차순 정렬, b는 내림차순 정렬
a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    # 무조건 바꾸는 게 아니고 a의 값이 b의 값보다 작을 때만 바꿔야 됨
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
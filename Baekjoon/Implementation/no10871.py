# X보다 작은 수

n, x = map(int, input().split())
a = list(map(int, input().split()))

for data in a:
    if data < x:
        print(data, end=" ")
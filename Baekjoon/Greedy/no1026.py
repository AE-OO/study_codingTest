# 보물
# A를 정렬한 후 가장 작은 값부터 B의 가장 큰 값의 인덱스에 순서대로 넣음

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
result = 0
for data in a:
    result += (data * max(b))
    b.pop(b.index(max(b)))

print(result)
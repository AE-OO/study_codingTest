n,m = map(int, input().split())
numList = []
result = 0

# n X m의 크기의 배열을 만들어서 한 행 당 최솟값을 구한 후 최솟값들 사이의 최댓값을 구함
for i in range(n):
    numList.append(list(map(int, input().split())))
    num = min(numList[i])
    result = max(result, num)

print(result)


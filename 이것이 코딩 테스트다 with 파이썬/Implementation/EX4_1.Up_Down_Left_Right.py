# 생각
# 처음 좌표를 x = 1, y = 1으로 두고 L, R, U, D 가 나올 때마다 좌표에서 값을 더해가면 될 듯

# 구현
n = int(input())
directionList = list(input().split())
x = 1
y = 1

for i in range(len(directionList)):

    if directionList[i] == 'L':
        y2 = y - 1
    elif directionList[i] == 'R':
        y2 = y + 1
    elif directionList[i] == 'U':
        x2 = x - 1
    elif directionList[i] == 'D':
        x2 = x + 1

    if 1 <= x2 and x2 <= n and 1 <= y2 and y2 <= n:
        x = x2
        y = y2

print(x,y)
# 생각
# 처음 좌표를 x = 1, y = 1으로 두고 L, R, U, D 가 나올 때마다 좌표에서 값을 더해가면 될 듯

# 구현
n = int(input())
directionList = list(input().split())
x, y = 1, 1

for i in range(len(directionList)):
    if x < 1 or y < 1 or x > n or y > n:
        continue

    if directionList[i] == 'L':
        y -= 1
    elif directionList[i] == 'R':
        y += 1
    elif directionList[i] == 'U':
        x -= 1
    elif directionList[i] == 'D':
        x += 1
    print(f'({x},{y})')

print(x,y)
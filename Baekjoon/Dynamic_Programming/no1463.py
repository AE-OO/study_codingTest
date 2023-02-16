# 1로 만들기

x = int(input())
count = 0

x = x - 1
count = count + 1

while x != 1:
    if x % 3 == 0:
        x = x // 3
    elif x % 2 == 0:
        x = x // 2
    count = count + 1

print(count)
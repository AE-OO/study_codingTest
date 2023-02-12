# 설탕 배달

n = int(input())

a = [5, 3]
count = 0

while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n -= 3    # n이 5의 배수가 될 때까지 3을 뺌
    count += 1
else:
    print(-1)
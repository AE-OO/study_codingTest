# 설탕 배달
# 입력받은 값이 3과 5의 배수인지 확인 => 아니면 -1 출력
#

n = int(input())

a = [5, 3]
count = 0

while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)
n,k = map(int, input().split())
result = 0

# n이 1이 아니면 반복문을 계속 실행 (= n이 1이 되면 반복문 멈춤)
while n != 1:
    # 만약 n이 k의 배수가 아니라면
    if n % k != 0:
        # n이 k의 배수가 될 때까지 1을 뺌
        while n % k != 0:
            n -= 1
            result += 1
    # 만약 n이 k의 배수라면
    else:
        # n을 k로 나눈 몫이 1이 될 때까지 k로 계속 나눔
        n = n//k
        result += 1

print(result)
# ATM
# 무조건 시간이 짧은 사람 먼저 사용

n = int(input())
t = list(map(int, input().split()))

t.sort()
total = 0
time = []
time.append(t[0])

for i in range(1, n):
    time.append(time[i - 1] + t[i])

for i in time:
    total += i

print(total)
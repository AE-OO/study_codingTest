# 생각
# h, m, s를 선언해두고 h는 n까지 반복, m과 s는 59까지 반복해서 3이 들어가는 경우를 모두 세기

# 구현
n=int(input())
h, m, s, count = 0, 0, 0, 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1
print(count)
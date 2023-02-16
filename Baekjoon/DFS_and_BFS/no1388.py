# 바닥 장식
# 함수 안에서 함수 호출하는 식으로 구현하면 안될듯
# 수정

def rowShape(i, j, count):
    for a in range(m):
        if shape[i][a] == '|':
            count = count + 1
            colShape(i, a, count)
        count = count + 1
        print(a,' ', count)
    return count


def colShape(i, j, count):
    for a in range(n):
        if shape[a][j] == '-':
            count = count + 1
            rowShape(a, j, count)
        count = count + 1
        print(a,' ', count)
    return count


n, m = map(int, input().split())  # n 세로, m 가로
shape = []

for _ in range(n):
    shape.append(list(input()))

print(rowShape(0, 0, 0))
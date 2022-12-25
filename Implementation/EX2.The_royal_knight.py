# 생각
# 나이트가 이동할 수 있는 경우를 모두 찾아서 리스트에 넣고 그 경우가 가능할 때 카운트 증가
# 주어진 좌표는 문자X숫자 형태 -> 문자를 숫자로 바꿔야 함 -> 알파벳을 숫자로 변환하는 함수 ord()

# 구현
coordinate = input()
x = int(ord(coordinate[0]))   # 열 98
y = int(coordinate[1])   # 행
count = 0

knightCoordi = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (2, -1), (2, 1), (-1, -2), (1, -2)]

for case in knightCoordi:
    x2 = x + case[1]
    y2 = y + case[0]
    print(x2, y2)
    if x2 >= 98 or y2 >= 1 or x2 <= 104 or y2 <= 8:
        count += 1
print(count)

# 삽입 정렬 소스 코드 - 데이터가 거의 정렬 되어 있는 경우
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 삽입 정렬은 1번째 인덱스에서부터 비교를 함 - 0번째 인덱스는 이미 정렬된 것으로 보기 떄문
for i in range(1, len(array)):
    # i번째 인덱스에서부터 하나씩 인덱스를 줄여가면서 값을 비교함
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
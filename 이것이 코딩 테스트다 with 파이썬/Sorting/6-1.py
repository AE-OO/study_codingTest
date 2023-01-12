# 선택 정렬 소스 코드 - 특정한 리스트에서 가장 작은 데이터를 찾을 때 주로 사용
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 처음에는 인덱스 0의 값을 가장 작은 수라고 둠
    min_index = i
    for j in range(i + 1, len(array)):
        # i 이후의 인덱스 값을 i 인덱스의 값과 비교하면서 실제로 가장 작은 값이 몇번째 인덱스에 있는지 찾음
        if array[min_index] > array[j]:
            min_index = j
        # swap
        array[i], array[min_index] = array[min_index], array[i]

print(array)
# 파이썬의 장점을 살린 퀵 정렬 소스코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 가지고 있다면 재귀 종료
    if len(array) <= 1:
        return array
    
    # 기준값을 0번째 인덱스의 값으로 줌
    pivot = array[0]
    # 기준값을 제외한 값만 가지는 리스트
    tail = array[1:]

    # 왼쪽은 기준값보다 작은 값들을 포함한 리스트
    left_side = [x for x in tail if x <= pivot]
    
    # 오른쪽은 기준값보다 큰 값들을 포함한 리스트
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
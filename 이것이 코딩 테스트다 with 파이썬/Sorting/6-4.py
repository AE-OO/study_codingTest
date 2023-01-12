# 퀵 정렬 소스 코드 - 기준(피벗)을 설정하고 큰 수와 작은 수를 교환한 후 리스트를 반으로 나눔

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 기준 뒤의 값들이 1개 남았을 경우 종료
    if start >= end:
        return
    # 첫번째 인덱스 값을 기준으로 둠
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 기준보다 큰 값을 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 기준보다 작은 값을 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 만약 왼쪽 값과 오른쪽 값이 엇갈렸다면 작은 데이터(오른쪽 값)과 기준을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터(오른쪽 값)과 큰 데이터(왼쪽 값)을 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할된 후 기준 왼쪽의 리스트와 오른쪽의 리스트 각각에서 다시 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
    
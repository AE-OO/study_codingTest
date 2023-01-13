# 재귀 함수로 구현한 이진 탐색 소스 코드
# 이진 탐색 - 시작점, 중간점((시작점+끝점)/2), 끝점을 두고 찾으려는 값과 중간값을 비교해 감, 정렬된 리스트에서 유리

def binary_search(array, target, start, end):
    # 찾고자 하는 값이 리스트에 없으면 none을 리턴하고 재귀 종료
    if start > end:
        return None
    mid = (start + end) // 2
    # 중간값과 찾고자 하는 값이 같으면 중간값의 인덱스 리턴
    if array[mid] == target:
        return mid

    # 중간값보다 찾고자 하는 값이 작다면 중간값 기준 왼쪽의 리스트들로 다시 중간값과 끝점을 설정 후 재귀
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    # 중간값보다 찾고자 하는 값이 크다면 중간값 기준 오른쪽의 리스트들로 다시 시작점과 중간점을 설정 후 재귀
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
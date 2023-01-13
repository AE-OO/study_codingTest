n, m = map(int, input().split())
h_list = list(map(int, input().split()))

start = 0
end = max(h_list)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in h_list:
        # 중간값보다 떡 길이가 더 긴 경우 => 떡을 잘라서 자른 것들끼리의 합을 구함
        if i > mid:
            total += i - mid
    # 자른 것들의 합이 목표로 했던 길이보다 작으면 중간점을 왼쪽으로 옮겨서 다시 탐색
    if total < m:
        end = mid - 1
    # 자른 것들의 합이 목표로 했던 길이보다 크면 일단 그 값을 저장해두고 최댓값을 구하기 위해 중간점을 오른쪽으로 옮겨서 다시 탐색
    else:
        result = mid
        start = mid + 1

print(result)
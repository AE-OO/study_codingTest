# 생각
# max()를 사용해 리스트의 최댓값을 구해야겠다고 생각 -> 두번째로 큰 수를 구하는 방법을 떠올리지 못함 -> 책 보고 sort 사용하는 거 힌트 얻음
# [큰 수 k번 + 두번째 큰 수 1번] 의 세트가 반복될 것임
# 세트가 들어가고 남는 값이 있다면 큰 수를 남는 값만큼 더하면 가장 큰 결과를 반환할 수 있음

# 구현
n,m,k = map(int, input().split())
numList = list(map(int, input().split()))
result = 0

# 여러 개의 숫자 중 일부를 더해서 가장 큰 수를 만드려면 가장 큰 수와 그 다음 수를 더해나가면 됨
# 정렬을 해서 가장 큰 수와 두번째로 큰 수를 구함
numList.sort()
first = numList[n-1]
second = numList[n-2]

# 인덱스가 같은 수를 k번 초과해서 더할 수 없기 떄문에 [큰 수 k번 + 두번째 큰 수 1번] 의 세트가 반복될 것임
# m//k를 해서 세트가 몇 번 반복되어야 하는지 구함
for i in range(m//k):
    result += (first*k + second)

# 세트가 딱 맞게 떨어지지 않는다면 나머지만큼 큰 수를 더 더해줌
if (m%(k+1)) != 0:
    result += first*(m%k)

print(result)
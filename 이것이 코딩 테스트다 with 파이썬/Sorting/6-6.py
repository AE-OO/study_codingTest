# 계수 정렬 소스 코드 - 특정한 조건이 부합할 때(데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때) 사용
# 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트 생성(중복 신경 안씀)
# 리스트의 수가 몇 번 등장했는지를 저장 ex) 028232 에서 0은 1번, 1은 0번, 2는 3번... 과 같은 식으로
# 저장된 횟수만큼 인덱스를 출력 ex) 위의 예에서 0은 1번, 1은 0번, 2는 3번... 나왔으니까 0222... 와 같은 식으로

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# array에 포함된 숫자의 범위가 모두 담길 수 있는 리스트 생성
count = [0] * (max(array) + 1)

# 각 인덱스에 해당하는 수가 몇 개 있는지 셈
for i in range(len(array)):
    count[array[i]] += 1

# 그 갯수만큼 인덱스를 출력함
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end='')
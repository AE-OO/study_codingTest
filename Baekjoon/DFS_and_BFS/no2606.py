# 바이러스
# 1번과 연결된 컴퓨터 수들 먼저 구하고, 그 애들이랑 연결된 컴퓨터 수를 또 구하고

def dfs(i) :
    visited[i] = 1        # 방문한 노드는 1로 바꿈
    for a in node[i]:
        if visited[a] == 0:  # i번째 노드와 연결된 노드 중 방문하지 않은 노드가 있다면 dfs() 함수 다시 실행해서 방문함
            dfs(a)


n = int(input())                  # 총 컴퓨터 수
l = int(input())                  # 연결선 수
node = [[] for _ in range(n + 1)] # 노드에 연결된 정보 저장
visited = [0] * (n + 1)           # 방문 여부 저장
count = 0                         # 바이러스 감염된 컴퓨터 수 구함

for i in range(l):                # 각 컴퓨터에 연결된 컴퓨터 정보 저장
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

dfs(1)                            # 깊이 우선 탐색 함수 실행 (시작점은 문제에서 1로 주어짐)

for i in visited:
    if i == 1:
        count += 1
        
print(count - 1)  # visited의 0번째 인수는 허수니까 -1
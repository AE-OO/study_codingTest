# 간단한 다익스트라 알고리즘 소스코드

import sys
input = sys.stdin.readline
INF = int(1e9) # 노드 간 거리가 정해지지 않은 경우엔 무한을 의미하는 10억을 값으로 설정

# 노드 및 간선 갯수
n,m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 각 노드에 연결된 노드 정보 담는 리스트
graph = [[] for i in range(n + 1)]
# 방문한 적 있는 노드인지 판별
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # 'a에서 b로 가는데 c의 거리가 걸림'을 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중 최단 거리인 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # start 노드와 연결된 모든 노드를 봄
        distance[j[0]] = j[1] # 연결된 노드의 비용(c)를 기록

    for i in range(n - 1):
        now = get_smallest_node()
        # 현재 최단 거리인 노드를 방문했다고 처리함
        visited[now] = True

        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1] # 연결된 노드로의 비용을 하나씩 보면서 비용을 더해줌

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost # 시작 노드에서 j[0]의 노드까지 가는 비용을 최소로 갱신

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
# DFS와 BFS
# DFS는 재귀호출을 통해 구현 -
# BFS는 큐와 반복문을 통해 구현 - 방문해야 하는 곳을 큐에 저장하고, 큐에서 빼면서 노드 방문

def DFS(v):
    visited[v] = 1
    dfs.append(v)
    for i in node[v]:
        if visited[i] == 0:
            DFS(i)


def BFS(v):
    visited[v] = 1
    bfs.append(v)     # 여기 오류
    queue = [v]

    while (queue):
        for i in node[queue.pop[0]]:
            if visited[i] == 0:
                visited[i] = 1
                bfs.append(i)
                queue.append(i)

n, m, v = map(int, input().split());
node = [[]for _ in range(n+1)]
visited = [0] * (n+1)
dfs = []
bfs = []

# 각 노드에 연결된 노드를 리스트로 정리함  [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
for i in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


DFS(v)
for j in range(n+1):
    visited[j] = 0

BFS(v)

for m in dfs:
    print(m, end=' ')
for n in bfs:
    print(n, end=' ')

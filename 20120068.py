import queue

adj = []
for i in range(0, 1010):
    adj.append([0] * 1010)

def dfs(here, visited):
    if visited[here] :
        return
    visited[here] = 1
    print(here, end =' ')
    for i in range(0, v + 1):
        if adj[here][i] and not visited[i] :
            dfs(i, visited)

v, e, start = map(int, input().split())
for i in range(0, e):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

visited = [0] * (v + 1)
dfs(start, visited)
print()

q = queue.Queue()
visited = [0] * (v + 1)
visited[start] = 1
q.put(start)
while q.qsize() :
    SIZE = q.qsize()
    for i in range(0, SIZE):
        here = q.get()
        for j in range(0, v + 1):
            if adj[here][j] and not visited[j] :
                visited[j] = 1
                q.put(j)
        print(here, end = ' ')
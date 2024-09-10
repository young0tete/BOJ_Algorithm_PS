import heapq
import sys

input=sys.stdin.readline

def find (x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) 
    return parent[x]

def union(a, b, cost):
    #그래프도 연결
    if a in graph.keys():
        graph[a].append((b, cost))
    else:
        graph[a]=[(b, cost)]
    if b in graph.keys():
        graph[b].append((a, cost))
    else:
        graph[b]=[(a, cost)]
        
    a = find(a)
    b = find(b)

    if a < b: 
        parent[b] = a
    else:
        parent[a] = b 

def same(a, b):
    return find(a) == find(b)

def dfs(u, p):
    result = (0, u)
    for v, w in graph[u]:
        if v == p:
            continue
        dist, far = dfs(v, u)
        result = max(result, (dist + w, far))
    return result

n,k=map(int, input().split())
q=[]
parent=[i for i in range(n)]
graph={}

for _ in range(k):
    a, b, c=map(int, input().split())
    heapq.heappush(q, (c, a, b))
    
link_cost=0

while q:
    c,a,b=heapq.heappop(q)
    if not same(a, b):
        link_cost+=c
        union(a, b, c)

_, far = dfs(0, -1)

print(link_cost)
print(dfs(far, -1)[0]) 
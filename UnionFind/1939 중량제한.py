import heapq
import sys

input=sys.stdin.readline

def find (x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) 
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b: 
        parent[b] = a
    else:
        parent[a] = b        

def same(a, b):
    return find(a) == find(b)

n, m=map(int, input().split())
parent=[i for i in range(n+1)]
q=[]

for _ in range(m):
    a,b,c=map(int, input().split())
    heapq.heappush(q, (-c, a, b))
f1, f2=map(int, input().split())
    
weight=0
while q:
    if same(f1, f2):
        break
                
    c,a,b=heapq.heappop(q)
    weight=-c
    union(a, b)
        
print(weight)
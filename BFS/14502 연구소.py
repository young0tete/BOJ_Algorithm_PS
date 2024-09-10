import itertools
import copy
from collections import deque
import sys

def bfs (matrix, r, c):
    global R, C
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    
    q=deque()
    q.append((r, c))
    
    while q:
        row, col=q.popleft()     
        matrix[row][col]=2
        for i in range(4):
            nr, nc=row+dr[i], col+dc[i]
            if (0<=nr<R) and (0<=nc<C):
                if matrix[nr][nc]==0:
                    q.append((nr, nc)) 


R, C=map(int, sys.stdin.readline().split())
mat=[]
li=[]
for i in range(R):
    r=list(map(int, sys.stdin.readline().split()))
    mat.append(r)
    for idx, j in enumerate(r):
        if j==0:
            li.append([i,idx])
            
cases=list(itertools.combinations(li, 3))
ans=0
for case in cases:
    matrix=copy.deepcopy(mat)
    matrix[case[0][0]][case[0][1]]=1
    matrix[case[1][0]][case[1][1]]=1
    matrix[case[2][0]][case[2][1]]=1
    
    for i in range(R):
        for j in range(C):
            if matrix[i][j]==2:
                bfs(matrix, i, j)
                
    safe=sum(row.count(0) for row in matrix)
    if safe>ans:
        ans=safe
        ans_mat=copy.deepcopy(matrix)
        
print(ans)
import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy


direction = {
    1: (0, 1),
    2: (-1, 1),
    3: (-1, 0),
    4: (-1, -1),
    5: (0, -1),
    6: (1, -1),
    7: (1, 0),
    8: (1, 1)
}

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

growth = deque([(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)])

d_lst = [list(map(int, input().split())) for _ in range(m)]

for d, p in d_lst:
    di, dj = direction[d]
    
    # 1. 특수 영양제 이동
    L = len(growth)
    
    for _ in range(L):
        i, j = growth.popleft()

        ni, nj = (i + di * p) % n, (j + dj * p) % n

        growth.append((ni, nj))
        
    # 2. 특수 영양제 위치 리브로수 성장
    for i, j in growth:
        arr[i][j] += 1
    
    # 3. 주변 위치에 따른 성장
    for i, j in growth:
        
        for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj]:
                    arr[i][j] += 1
    
    # 4. 2 이상의 리브로수 잘라낸 후 특수 영양제 투하
    
    new_growth = deque([])
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i, j) not in growth:
                arr[i][j] -= 2
                
                new_growth.append((i, j))
    
    growth = deepcopy(new_growth)
    
ans = 0

for i in range(n):
    ans += sum(arr[i])
    
print(ans)
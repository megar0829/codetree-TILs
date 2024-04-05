from copy import deepcopy

n, m, k, c = map(int, input().split())


# arr : 나무, herbicide : 제초제
arr = [list(map(int, input().split())) for _ in range(n)]
herbicide = [[0] * n for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == -1:
            herbicide[i][j] = -1

for _ in range(m):
    # 1. 나무의 성장

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > 0:
                        arr[i][j] += 1

    # for i in range(n):
    #     print(*arr[i])

    # print('==============================')


    # 2. 나무의 번식

    save_arr = deepcopy(arr)

    for i in range(n):
        for j in range(n):
            if save_arr[i][j] > 0:
                cnt = 0

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < n and 0 <= nj < n:
                        if save_arr[ni][nj] == 0 or (save_arr[ni][nj] == -1 and herbicide[ni][nj] == 0):
                            cnt += 1

                if cnt:
                    spread_val = arr[i][j] // cnt

                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        
                        if 0 <= ni < n and 0 <= nj < n:
                            if save_arr[ni][nj] == 0 or (save_arr[ni][nj] == -1 and herbicide[ni][nj] == 0):
                                arr[ni][nj] += spread_val
                
    # for i in range(n):
    #     print(*arr[i])

    # print('==============================')

    # 3. 제초제를 뿌릴 위치 선정

    max_val = 0
    max_idx = (0, 0)

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                save_val = arr[i][j]

                for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                    for leng in range(1, k + 1):
                        ni, nj = i + di * leng, j + dj * leng

                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] >= 0:
                                save_val += arr[ni][nj]

                            elif arr[ni][nj] == -1 and herbicide[ni][nj] != -1:
                                continue
                            
                            else:
                                break

                        else:
                            break
                
                if max_val < save_val:
                    max_val = save_val
                    max_idx = (i, j)

    # print(max_val)
    # print(max_idx)


    # 4. 제초제를 뿌리는 작업 진행

    i, j = max_idx

    ans += arr[i][j]
    arr[i][j] = -2
    herbicide[i][j] = c

    for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
        for leng in range(1, k + 1):
            ni, nj = i + di * leng, j + dj * leng

            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] >= 0 or (arr[ni][nj] == -1 and herbicide[ni][nj] != -1):
                    ans += arr[ni][nj]
                    arr[ni][nj] = -2
                    herbicide[ni][nj] = c
                
                else:
                    break

            else:
                break

                
    # for i in range(n):
    #     print(*arr[i])

    # print('==============================')


    # 5. 제초제 연도 감소

    for i in range(n):
        for j in range(n):
            if arr[i][j] == -2:
                arr[i][j] = -1
            
            elif herbicide[i][j] > 0:
                herbicide[i][j] -= 1

    # for i in range(n):
    #     print(*arr[i])

    # print('==============================')

    # for i in range(n):
    #     print(*herbicide[i])

    # print('==============================')

print(ans)
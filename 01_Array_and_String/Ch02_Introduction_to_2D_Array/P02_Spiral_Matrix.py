def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    # 방문기록
    visited = [[False for _ in range(n)] for _ in range(m)]
    # 우 하 좌 상
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    dir = 0
    dir_times = 0
    ans = []
    x, y = 0, 0
    ans.append(matrix[x][y])
    visited[x][y] = True
    while dir_times<2:
        nx = x + directions[dir][0]
        ny = y + directions[dir][1]
        if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
            ans.append(matrix[nx][ny])
            visited[nx][ny] = True
            dir_times=0
            # 다음 위치로 초기화
            x, y = nx, ny
        else: 
            dir = (dir+1) % 4
            dir_times += 1
    return ans

def review_20220926(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    VISITED = 101
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    dir = 0
    dir_times = 0
    ans = []
    x, y = 0, 0
    ans.append(matrix[x][y])
    matrix[x][y] = VISITED

    while dir_times<2:
        nx = x + directions[dir][0]
        ny = y + directions[dir][1]
        if 0<=nx<rows and 0<=ny<cols and matrix[nx][ny] != VISITED:
            ans.append(matrix[nx][ny])
            matrix[nx][ny] = VISITED
            x, y = nx, ny
            dir_times=0
        else:
            dir = (dir+1) % 4
            dir_times += 1
    return ans
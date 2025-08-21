from collections import deque

n = int(input())
grid = []
result = 0
cnt_arr = []


def bfs(grid, start_x, start_y, visited):
    cnt = 1
    # 상하좌우 방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    cnt += 1
                    visited[nx][ny] = True
    return cnt


for _ in range(n):
    grid.append(list(map(int, input())))
visited = [[False for _ in range(n)] for _ in range(n)]

for x in range(n):
    for y in range(n):
        if grid[x][y] == 1 and not visited[x][y]:
            cnt_arr.append(bfs(grid, x, y, visited))
            result += 1

print(result)
cnt_arr.sort()
for c in cnt_arr:
    print(c)

from collections import deque

def min_cookies_for_escape_interactive():
    rows, cols = map(int, input().split())

    maze = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        maze.append(row)

    # Initialize the dp array with infinity and set the starting point
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = maze[0][0]

    # Use BFS to update the dp array
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if dp[nx][ny] > dp[x][y] + maze[nx][ny]:
                    dp[nx][ny] = dp[x][y] + maze[nx][ny]
                    queue.append((nx, ny))

    # The minimum number of cookies required to escape
    return dp[rows - 1][cols - 1]

result = min_cookies_for_escape_interactive()
print(result)
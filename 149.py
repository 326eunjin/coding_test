ret = 0
n, m = map(int, input().split())
# arr = [[0] * m in range(n)]
global arr
arr = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))


def dfs(n, m):
    for i in range(n):
        for j in range(m):

            # def make_graph


for i in range(n):
    for j in range(m):
        graph = dfs(arr, n, m)
        if dfs()

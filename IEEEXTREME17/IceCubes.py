"""
3
2 3 2 5
6 6 1
1 1 5
3 4 3 7
5 5 6 5
3 6 3 5
7 1 8 4
4 4 3 6
9 5 3 3
9 1 1 5
3 1 3 5
1 1 3 2
"""

def _ricorsive(grid, N, M, K, B, i, j, cons_bad):
    if cons_bad == -1:
        return -10e15
    cons_bad = cons_bad -1 if grid[i][j] < B else K
    
    if i == N - 1 and j == M - 1:
        return grid[i][j]
    elif i == N - 1:
        return grid[i][j] + _ricorsive(grid, N, M, K, B, i, j + 1, cons_bad)
    elif j == M - 1:
        return grid[i][j] + _ricorsive(grid, N, M, K, B, i + 1, j, cons_bad)
    else:
        return grid[i][j] + max(_ricorsive(grid, N, M, K, B, i + 1, j, cons_bad), _ricorsive(grid, N, M, K, B, i, j + 1, cons_bad))


def solve_ricorsive():
	N, M, K, B = map(int, input().split())
	grid = []
	for _ in range(N):
		grid.append(list(map(int, input().split())))
	return _ricorsive(grid, N, M, K, B, 0, 0, K)
	

T = int(input())
for t in range(T):
    res = solve_ricorsive()
    if res >= 0:
        print(f"Case {t+1}: {res}")
    else:
        print(f"Case {t+1}: IMPOSSIBLE")
  

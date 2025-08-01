MOD = 10**9 + 7

# Compute Grundy number with memoization
def compute_grundy(board, n, d, memo):
    key = tuple(board)
    if key in memo:
        return memo[key]

    grundy_set = set()

    # Try all white pawn moves (1 moves right)
    for i in range(n):
        if board[i] == 1:
            for step in range(1, d + 1):
                ni = i + step
                if ni >= n or board[ni] != 0:
                    break
                new_board = board[:]
                new_board[i] = 0
                new_board[ni] = 1
                grundy_set.add(compute_grundy(new_board, n, d, memo))

    # Try all black pawn moves (2 moves left)
    for i in range(n):
        if board[i] == 2:
            for step in range(1, d + 1):
                ni = i - step
                if ni < 0 or board[ni] != 0:
                    break
                new_board = board[:]
                new_board[i] = 0
                new_board[ni] = 2
                grundy_set.add(compute_grundy(new_board, n, d, memo))

    # MEX calculation
    g = 0
    while g in grundy_set:
        g += 1

    memo[key] = g
    return g

# Generate combinations without itertools
def generate_combinations(arr, r):
    res = []
    def backtrack(start, path):
        if len(path) == r:
            res.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return res

# Main solve function
def solve(n, k, d):
    if k % 2 != 0:
        return 0  # Invalid, must be even

    half_k = k // 2
    result = 0
    positions = []

    # Generate all combinations of K positions on N cells
    def backtrack(start, path):
        if len(path) == k:
            positions.append(path[:])
            return
        for i in range(start, n):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])

    for pos in positions:
        white_combinations = generate_combinations(pos, half_k)
        for white_pos in white_combinations:
            board = [0] * n
            for w in white_pos:
                board[w] = 1
            for b in pos:
                if b not in white_pos:
                    board[b] = 2
            memo = {}
            g = compute_grundy(board, n, d, memo)
            if g != 0:
                result = (result + 1) % MOD

    return result

# Input/Output
def main():
    n, k, d = map(int, input().split())
    print(solve(n, k, d))

# Run main
main()

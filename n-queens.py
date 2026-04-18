def solve_n_queens(n):

    #  Simple error handlin for invalid input
    if not isinstance(n, int) or n < 1:
        print("Invalid input! N must be a positive integer.")
        return

    #  Create empty board (2D array)
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []


    def is_safe(row, col):
        
        #  Check column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        #  Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        #  Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    #  Backtracking function
    def backtrack(row):
        if row == n:
            solutions.append([" ".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"   
                backtrack(row + 1)      
                board[row][col] = "."   

    backtrack(0)


    # Results logic build
    if not solutions:
        print(f"No solutions exist for N = {n}")
        return

    print(f"\nTotal Solutions for N = {n}: {len(solutions)}\n")

    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        print("-" * (2 * n))
        for row in sol:
            print(row)
        print("-" * (2 * n))
        print()


n = int(input("Enter value of N: "))
solve_n_queens(n)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        result = []

        board = [["."] * n for _ in range(n)]

        def is_safe(row, col):

            # Check same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper-left diagonal
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):

            # All queens placed
            if row == n:
                solution = []

                for r in board:
                    solution.append("".join(r))

                result.append(solution)
                return

            # Try every column in this row
            for col in range(n):

                if is_safe(row, col):

                    # Place queen
                    board[row][col] = "Q"

                    # Move to next row
                    backtrack(row + 1)

                    # Remove queen (Backtrack)
                    board[row][col] = "."

        backtrack(0)

        return result
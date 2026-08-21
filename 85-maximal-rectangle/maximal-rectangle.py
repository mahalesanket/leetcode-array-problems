class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in range(rows):

            # Build histogram for current row
            for col in range(cols):

                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            # Find largest rectangle in histogram
            stack = [-1]

            for i in range(cols):

                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:

                    h = heights[stack.pop()]
                    width = i - stack[-1] - 1

                    max_area = max(max_area, h * width)

                stack.append(i)

            # Clear remaining bars
            while stack[-1] != -1:

                h = heights[stack.pop()]
                width = cols - stack[-1] - 1

                max_area = max(max_area, h * width)

        return max_area
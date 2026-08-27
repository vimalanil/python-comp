class Solution:
    def generateMatrix(self, n):

        matrix = [[0] * n for _ in range(n)]

        top = 0
        left = 0
        right = n - 1
        bottom = n - 1

        pos = 1

        while top <= bottom and left <= right:

            # Left → Right
            for i in range(left, right + 1):
                matrix[top][i] = pos
                pos += 1

            top += 1

            # Top → Bottom
            for j in range(top, bottom + 1):
                matrix[j][right] = pos
                pos += 1

            right -= 1

            # Right → Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = pos
                    pos += 1

                bottom -= 1

            # Bottom → Top
            if left <= right:
                for j in range(bottom, top - 1, -1):
                    matrix[j][left] = pos
                    pos += 1

                left += 1

        return matrix


# User input
n = int(input("Enter n: "))

obj = Solution()

result = obj.generateMatrix(n)

# Print matrix
for row in result:
    print(*row)
#%%
# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        nrows = []
        for i in range(numRows):
            one_row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    one_row.append(1)
                else:
                    one_row.append(nrows[i-1][j-1]+nrows[i-1][j])
            
            nrows.append(one_row)
        return nrows

Solution().generate(5)


# %%
# 119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [0] * (rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i,-1,-1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = row[j-1] + row[j]
            #     print(row)
            # print()
        return row

Solution().getRow(5)


# %%
# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_1 = False
        col_1 = False

        for i in range(m):
            if matrix[i][0] == 0:
                row_1 = True
                break

        for i in range(n):
            if matrix[0][i] == 0:
                col_1 = True
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_1:
            for i in range(m):
                matrix[i][0] = 0

        if col_1:
            for i in range(n):
                matrix[0][i] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)

# %%
# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        lst = []
        while len(matrix) > 1 and len(matrix[0]) > 1:
            lst.extend(matrix.pop(0))
            for i in range(len(matrix)):
                lst.append(matrix[i].pop(-1))

            lst.extend(reversed(matrix.pop(-1)))
            if matrix:
                for i in range(len(matrix)-1, -1, -1):
                    lst.append(matrix[i].pop(0))
            else:
                break
        
        if matrix:
            if len(matrix) == 1:
                lst.extend(matrix.pop(0))
            elif len(matrix[0]) == 1:
                for i in matrix:
                    lst.append(i[0])

        return lst





# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,3],[4,5]]
Solution().spiralOrder(matrix)
# %%
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        ans = []

        while True:
            for i in range(left, right+1):
                ans.append(matrix[up][i])
            up += 1
            if up > down:
                break

            for i in range(up, down+1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left-1, -1):
                ans.append(matrix[down][i])
            down -= 1
            if up > down:
                break

            for i in range(down, up-1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        
        return ans

matrix = [[1,3],[4,5]]
Solution().spiralOrder(matrix)
# %%
# 498. Diagonal Traverse
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        up, down, left, right = 0, len(mat)-1, 0, len(mat[0])-1
        x = y = 0
        ans = []

        while x <= down and y <= right:
            ans.append(mat[x][y])
            if (x+y)%2:
                if x+1 > down:
                    y += 1
                elif y-1 < left:
                    x += 1
                else:
                    x += 1
                    y -= 1
            else:
                if y+1 > right:
                    x += 1
                elif x-1 < up:
                    y += 1
                else:
                    x -= 1
                    y += 1
        
        return ans
        
matrix = [[1,3],[4,5]]
Solution().findDiagonalOrder(matrix)

# %%
# 48. Rotate Image

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for m in matrix:
            left = 0
            right = n - 1
            while left < right:
                tmp = m[left]
                m[left] = m[right]
                m[right] = tmp
                left += 1
                right -= 1

        for i in range(n-1):
            for j in range(n-1-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = tmp

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
print(matrix)

# %%
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1

        # y -> x
        # n-x -> y
        for x in range((n+1)//2):
            for y in range(x, n-x):
                tmp = matrix[x][y]
                matrix[x][y] = matrix[n-y][x]
                matrix[n-y][x] = matrix[n-x][n-y]
                matrix[n-x][n-y] = matrix[y][n-x]
                matrix[y][n-x] = tmp


# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[5,1,9,11,3],[2,2,4,8,10],[3,13,3,6,7],[4,15,14,12,16],[4,15,14,12,16]]

Solution().rotate(matrix)
print(matrix)
# %%
# 289. Game of Life
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:

        directions = {(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)}


        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                lives = 0
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]

                    if 0 <= new_row < rows and 0 <= new_col < cols and abs(board[new_row][new_col]) == 1:
                        lives += 1

                if board[row][col] == 1 and (lives<2 or lives>3):
                    board[row][col] = -1
                if board[row][col] == 0 and lives == 3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1

Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

# %%

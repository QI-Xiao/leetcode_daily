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

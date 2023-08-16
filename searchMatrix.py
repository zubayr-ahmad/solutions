# https://leetcode.com/problems/search-a-2d-matrix/
def getTargetRow(matrix,height,width):
    for i in range(height):
        if target <= matrix[i][width - 1]:
            return i
    return None
def searchMatrix(matrix, target):
    height = len(matrix)
    width = len(matrix[0])
    targetRow = getTargetRow(matrix,height,width)
    if targetRow == None:
        return False

    for j in range(width):
        if target == matrix[targetRow][j]:
            return True
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 20
    print(searchMatrix(matrix, target))

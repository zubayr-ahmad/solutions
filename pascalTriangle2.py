# https://leetcode.com/problems/pascals-triangle-ii/
def generate(rowIndex):
    triangle = [[1], [1, 1]]
    if rowIndex == 0:
        return triangle[0]
    elif rowIndex == 1:
        return triangle[1]
    else:
        for i in range(1, rowIndex):
            row = createRow(triangle[i])
            triangle.append(row)
    return triangle[-1]


def createRow(lastRow):
    row = []
    for i in range(1, len(lastRow)):
        val = lastRow[i - 1] + lastRow[i]
        row.append(val)
    row.append(1)  # append first and last 1s
    row.insert(0, 1)
    return row


if __name__ == '__main__':
    rowIndex = 3
    print(generate(rowIndex))

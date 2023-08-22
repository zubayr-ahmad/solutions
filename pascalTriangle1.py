# https://leetcode.com/problems/pascals-triangle/
def generate(numRows):
    triangle = [[1],[1,1]]
    if numRows == 1:
        return [triangle[0]]
    elif numRows == 2:
        return triangle
    else:
        for i in range(2,numRows):
            row = createRow(triangle[i-1])
            triangle.append(row)
    return triangle

def createRow(lastRow):
    row = []
    for i in range(1,len(lastRow)):
        val = lastRow[i-1]+lastRow[i]
        row.append(val)
    row.append(1)   # append first and last 1s
    row.insert(0,1)
    return row

if __name__ == '__main__':
    numRows = 111
    print(generate(numRows))
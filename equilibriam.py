def equiblibrium(arr):
    x,y,z = 0,0,0
    for i in arr:
        x += i[0]
        y += i[1]
        z += i[2]

    if x == 0 and y == 0 and z == 0:
        return "YES"
    else:
        return "NO"



noOfVectors = int(input())
vectors = []
for i in range(noOfVectors):
    vectors.append(list(map(int,input().split())))

print(equiblibrium(vectors))
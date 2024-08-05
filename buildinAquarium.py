# https://codeforces.com/problemset/problem/1873/E

def returnHeight(cols,water):
    h = 0
    cols.sort()
    for i,val in enumerate(cols):
        if water != 0 and val < cols[i+1]:
            cols[i] += 1
            water -= 1
            continue
        break
    ...


if __name__ == "__main__":
    no_of_test_cases = int(input())
    tests = []
    for i in range(no_of_test_cases):
        no_of_cols,max_water = list(map(int,input().split()))
        cols = list(map(int,input().split()))
        tests.append((no_of_cols,max_water,cols))

    

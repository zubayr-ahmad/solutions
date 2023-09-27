def findHello(string):
    goal = "hello"
    pointer = goal[0]


    j = 0
    for i in string:
        if i == pointer:
            try:
                pointer = goal[j+1]
            except:
                return "YES"
            j += 1

    return 'NO'


string = input()        
print (findHello(string))

    


            
        

        


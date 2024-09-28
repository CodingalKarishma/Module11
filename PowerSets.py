def printPowerSet(set, set_size):
    power_set_size = 2**set_size
    outer = 0
    inner = 0
    for outer in range(0, power_set_size):
        for inner in range(0,SetSize):
            if((outer & (1<<inner))==0):
                print(set[inner],end="")
            print("")
    size=int(input("Enter Array Size"))
    set=[]
    for i in range(0,size):
        n=int(input("Enter Number"))
        set.append(n)
    printPowerSet(set,len(sat))

  
    
        


  
                                
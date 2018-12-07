def check(grid):
    val = "safe"
    #print(len(grid))
    grid_len = len(grid)
    #print("grid_len:"+str(grid_len))
    main_set = set()
    for i in range(grid_len):
        if (grid[i]== '.'):
            continue
        length = int(grid[i])
        #print("length:"+str(length))
        arr1 = []
        start_point = i - length
        if(start_point < 0):
            start_point = 0
        #print("start_point:"+str(start_point))
        #end_point = start_point + (length*2)+ 1
        end_point = i + length
        if(end_point > grid_len):
            end_point = grid_len
        #print("end_point:",end_point)
        for j in range((end_point - start_point)+1):
            arr1.append(start_point)
            start_point +=1
        new_set = set(arr1)
        #print(new_set)
        if(new_set.isdisjoint(main_set)):
            main_set = main_set.union(new_set)
        else:
            val = "unsafe"
            break
        #print(main_set)
        
    return val

n = int(input())
for _ in range(n):
    grid = (input())
    print(check(grid))


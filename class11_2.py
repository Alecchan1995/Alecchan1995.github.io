a = [10,25,31]
for i in range(len(a)): #0-2 0 1 3
    for j in range(len(a)): # 0-2 
        if a[j] < a[i]: 
            t = a[i]
            a[i] = a[j]
            a[j] = t
        print(a)
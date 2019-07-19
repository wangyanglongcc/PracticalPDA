flag = True
for i in range(10):
    for j in range(10):
        if i+j==4:
            print(i,j)
            break
            flag = False
    if flag:
        break
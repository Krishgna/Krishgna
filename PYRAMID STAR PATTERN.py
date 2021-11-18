for i in range(1,5):
    for j in range(1,i+4):
        if j+i<=4:
            print(' ',end='')
        else:
            print('*',end='')
    print()
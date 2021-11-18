for i in range(0,5):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end=' ')
        k=k+1
    print()
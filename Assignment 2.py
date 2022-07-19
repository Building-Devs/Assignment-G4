while True:
    a=int(input('Enter value: '))
    if a==1:
        # this prints out the first element if a is 1
         print('*')
    for i in range(1,a):
        # range(1,a) removes the first step from the series       
        if i==1:
            print('*')
        # this is brought out since it does not follow the pattern required when added to the list
        for j in range (i+1):
            print('  *',end='')
        # i+1 shows the increasing of i from 1 to a
        print()

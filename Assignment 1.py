while True:
    n=int(input('Enter value: '))
    if n==1:
            print('    *')
    for i in range(1,n):
    # range(1,n) means, the first element in the series won't be printed since it would'nt follow the required pattern
        if i==1:
            print('    *')
    # this statement will print the first element and will be right in line with the required pattern     
        for j in range(3-i):
            print(' ',end=' ')
    # this statement prints a blank upside down triangle 
        for j in range(i+1):
            print('*',end=' ')
    # this prints a triangular pattern 
        print()



    
        
    

while True:
    num=int(input('Enter value: '))
    if num==1:
            for j in range(num):
                print(' ',end='')
            for j in range(1):
                print('*')
    #1 The above statement prints the first * but prints a 'num' number of times empty spaces before printing the *
    for i in range(num-1):
    #2 Since I separately will print out the first element of the series, the 1 is being subtracted from the range
        if i==0:
            for j in range(num):
                print(' ',end='')
            for j in range(1):
                print('*')
    #3 Similar statement to comment #1
        for j in range(num-i-1):
            print(end=" ")
        for j in range(1):
            print('*',end="")
    #4 This statement prints an empty space as num is decreased by i and 1 and prints *
        for j in range(2+2*i):
            print(end=" ")
        for j in range(1):
            print('*')
    #5 In range (2+2*i), for any value of i, it calculates the amount of spaces to produce and prints out *
            

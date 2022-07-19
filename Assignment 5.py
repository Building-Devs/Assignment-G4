number = int(input ("Number: "))
print(' ' * (number + 1) + '*')
i = 1
while i < number:
    print(' '*(number-i)+'* ' + ' '*(i - 1) + str(i) + ' '*(i - 1) + '*')
    i = i + 1


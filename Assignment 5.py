while True:
 n=int(input("Enter value: "))
 if n==1:
    print ("*")
 for i in range (1,n):
  if i==1:
    for j in range(n):
      print('  ',end="")
    for j in range(1):
      print("*")
  for j in range(n-i-1):
      print('  ',end="")
  for j in range(1):
      print("*",end="")
  for j in range(2*i+1):
      print(" ",end="")
  for j in range (1):
      print(i,end="")
  for j in range(i+1):
      print('  ',end="")
  for j in range(1):
        print('*')

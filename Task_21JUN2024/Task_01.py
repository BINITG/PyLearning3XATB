#RIGHT-ANGLE TRIANGLE STAR-PATTER(N=5)

n=int(input('Enter No Of Rows:'))
for i in range(n):
  for j in range(i+1):
    print('*',end=' ')
  print()

a = int(input("enter your number:"))
x = int(input('enter your first number in range:'))
y = int(input('enter your last number in range:'))
for i in range(x,y):
  if i%a==0:
    print(i)

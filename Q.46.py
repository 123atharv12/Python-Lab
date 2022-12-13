a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input('''Enter Operation : 
1. Add
2. Substract
3. Multiply
4. Divide'''))
if c==1:
    print(a+b)
if c==2:
    print(a-b)
if c==3:
    print(a*b)
if c==4:
    print(a/b)
#AtharvTamrakar
p=int(input("Enter initial principal balance : "))
r=int(input("Enter 	interest rate : "))
n=int(input("Enter number of times interest applied per time period : "))
t=int(input("Enter number of time periods elapsed : "))
e=n*t
f=r/n
d=p*1+f*e
print(d)
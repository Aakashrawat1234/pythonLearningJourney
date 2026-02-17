a=int(input("enter your first number"))
operator=input("enter operator (+,-,*,/,%):")
b=int(input("enter your second number"))

if operator == '+':
        print("your sum is",a+b)

elif operator =='-':
        print("your sub is",a-b)
                
elif operator =='*':
        print("your mul is",a*b)
elif operator =='/':
        print("your sub is",a/b)
else:
        print("enter a correct operator")        

print("thank you")


try:
    a=int(input("Enter your number"))
    print(f"Multiplication of table of {a} is:")
    for i in range(1,11):
        print(f"{a}x{i} ={a*i}")
except Exception as e:
    print("sorry some error occured ")


print("some imp lines of code")
print("End of program")    


try:
    num=int(input("Enter an integer:"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")    
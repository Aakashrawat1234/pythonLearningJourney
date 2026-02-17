for num in range(50):
    print(num+1)

print("next q")
for num in range(50):
    if num==0:
        continue
    if num%2==0:
        print(num)

print("next q")
i = 1
while i < 50:
    if i % 2 == 0:
        print(i)
    i += 1

    print("next q")



number=[1,2,3,4,5,6]

i=0
num1=0
while i<len(number):
    num1=num1+number[i]
    i=i+1
    
print(num)    
num3=0
for num2 in number:
    num3=num3+num2
    print(num3)




a=[1,2,3,4,5,4,4,2]


def count(b):
    count1=0
    for numCount in a:
        if numCount==b:
           count1=count1+1
    return count1          
            
    



print(count(4))

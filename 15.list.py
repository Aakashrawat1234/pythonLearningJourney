marks=[95,98,97]
print(marks[0])
print(marks[-1])# in python this means we are counting index backweord in this a=list it is 97
print(marks[0:2]) # this means include 0 to index 2 it wont include the last index


for score in marks:
    print(score)

marks.append(99) #add new entry at the end of string
print(marks)

marks.insert(3,98)  #insert at the specified index here 3 is index and 98 new entry
print(marks)

print(99 in marks) #finds if 99 present in marks

print(len(marks))  #gives lenght of the list

i=0

while i<len(marks):
    print(marks[i])
    i=i+1


    marks.clear() #clears the whole list
    
#file_object=open('filename','mode') to preform operation on file this function is used
#'r': Read(default mode). Open the file for reading.
#'w' Write.Opens the file for writinf(if file does not exist it creates one).
#'a': Append Opens the file for appending (if file doesn't exist it creates one).
#'rb'/'wb': Read/Write in binary mode


#Read from a file
#once a file is open,you can read from it using the following methods:
#read() Reads the entire content of the file
# readline():Reads one line from the file at a time
#readlines(): Reads all the lines into a list

# eg reading entire file
# file=open('example.txt','r')
# content=file.read()
# print(content)
# file.close()


# eg reading one line at a time
# file=open('example.txt','r')
# content=file.readLine()
# print(content)
# file.close()



#Write file
# To write a file ,you can use the write() or writelines() method:
# write(): writes a string to the file
# writeLines():writes a list of string

#eg writing to a file(overwrites existing content)
#file=open("eg.txt",'w')
#file.write("hello","world!")
#file.close()


#eg Appending to a file (add lines to the end
#file=open("eg.txt",'a')
#file.writelines("\n this an appended line")
#file.close()



#open file
file=open('eg.txt','r')

#read file
file=open('eg.txt','r')
content=file.read()
print(content)
file.close()

file=open('eg.txt','r')
first=file.readline()
print(first)
file.close()

file=open('eg.txt','r')
content1=file.readlines()
print(content1)
file.close()


#erite to a file
#file=open('eg2.txt','w')
#file.write("whats your name ,what ,that") is iw add multiple value they ovewrite so we use append
#file.close()



file=open('eg2.txt','a')
file.write("\nAcha hu")
file.close()


#close a file
#using with statement
with open('ex.txt','r') as file :
    content=file.read()
    print(content)


  #  Why do we use with?
 # 1. Automatically closes the file

  # No need to write file.close().

 #  2. Safer

 # If an error happens while reading, the file will still close properly.

 #  3. Cleaner code

 # Less code, more readable.

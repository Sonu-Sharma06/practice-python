#import os

#creting the file
open("first.txt","x")

#for write and appending the content into the file
f=open("second.txt","a")
f.write(" hiii this is sonu ")
f.close()

#for reading the content of the file
f=open("second.txt","rt")
text=f.read(5)
f.close()
print(text)

# for deleting the file
#os.remove("second.txt")



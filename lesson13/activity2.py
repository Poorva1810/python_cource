new_file=open("new_file.txt","x")
new_file.close()
import os
print("checking if my_file exists or not..")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exists")
my_file=open("my_file.txt","w")
my_file.write("this is a new file text")
my_file.close()
os.remove("codingal.txt")        
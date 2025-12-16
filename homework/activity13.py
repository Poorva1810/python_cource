with open("codingal1.txt","w")as file:
    file.write("a new text in the write mode")
file.close()
with open("codingal1.txt","r")as file:
    data=file.readlines()
    print("words in this file are..")
    for line in data:
        word =line.split() 
        print(word)
file.close()        

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
os.remove("codingal1.txt")  

outputFile=open("no_repeat1.txt","w")
inputFile=open("sample_doc1.txt")
lines_seen_so_far=set()
print("eliminating duplicate lines..")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
inputFile.close()
outputFile.close()        
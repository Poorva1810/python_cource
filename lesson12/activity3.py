file1=open("codingal2.txt","r")
file2=open("codingalupdated.txt","w")
for line in file1.readlines():
    if not (line.startswith('this')):
       print(line)
       file2.write(line)
file2.close()
file1.close()    
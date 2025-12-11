with open("codingal.txt","w")as file:
    file.write("a new text in the write mode")
file.close()
with open("codingal.txt","r")as file:
    data=file.readlines()
    print("words in this file are..")
    for line in data:
        word =line.split() 
        print(word)
file.close()        

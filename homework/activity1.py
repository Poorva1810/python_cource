present=float(input("total number of working days"))
absent=float(input("total number of days for absent"))
attendence=present/(present+absent/100)
if attendence<=75:
    print("student is eligible to give exam")
else: 
    print("student is not eligible to give exam")  


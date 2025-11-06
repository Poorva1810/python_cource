hight=float(input("enter your hight"))
weight=float(input("enter your weight"))
bmi=weight/(hight/100)**2
if bmi <=18.4:
    print("you are underweight")
elif bmi <=24.9:
    print("you are healthy") 
elif bmi <=29.9:
    print("you are overweight")
elif bmi <=34.9:
    print("you are severlyoverweight")
elif bmi <=39.9:
    print("you are obese") 
else:
    print("you are severlyobese")                  
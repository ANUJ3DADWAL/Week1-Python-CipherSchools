Name=input("Enter Your Name: ")
i=0
Variable=""
while i<len(Name):
    if Name[i] not in Variable:
       Variable+=Name[i]
       print(f"{Name[i]} : {Name.count(Name[i])}")
    i+=1
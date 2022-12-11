Full_Name,single=input("Enter your Full Name and One charcter for your name separated with commas :").split(",")
# print(f"Length of your name {len(Full_Name)} and Character in your name{Full_Name.count(single)}") This is the case of sensetive
print(f"Length of your name {len(Full_Name)} and character in your name : {Full_Name.lower() .count(single.lower())}")

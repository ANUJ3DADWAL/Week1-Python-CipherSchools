# Guessing no game
name="Welcome To Guessing Game"
print(name.center(len(name)+4,"*"))
Guessing_number=int(input("Enter your Guesssing Number: "))
Winning_number=17
if Guessing_number==Winning_number:
    print("You Win!")
elif Guessing_number>Winning_number:
    print("Guessing No is to high")
else:
    print("Guessing No is to low")        
    
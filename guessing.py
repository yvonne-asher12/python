#Yvonne Karimi
#BSCIT-05-0072/2024
winning_no = 5

guess_no = int(input("Enter the number: "))

while guess_no != winning_no:

    if guess_no < winning_no:
        print("Too low")
    else:
        print("Too high")

    guess_no = int(input("Try again: "))

print("YOU WIN!!!!")

    

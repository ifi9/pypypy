print("You are in a dark forest.")
choice1 = input("Do you go 'left' or 'right'? ").lower()

if choice1 == "left":
    print("You encounter a friendly elf who gives you a treasure!")
elif choice1 == "right":
    print("You fall into a trap. Game over.")
else:
    print("Invalid choice. Try again.")

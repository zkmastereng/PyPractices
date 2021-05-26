

print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure!\n")

choice_1 = input("You have to choose a side that you want to go. Type 'left' or 'right' !!!\n").lower()

if choice_1=="right":
    print("You fell into a hole! Game Over!")
elif choice_1=="left":
    choice_2 = input("Do you want to swim or wait?\n").lower()
    if choice_2=="swim":
        print("Attacked by trout! Game Over!")
    elif choice_2=="wait":
        choice_door=input("You have to choose a door. Options are 'Red', 'Blue' and 'Yellow\n").lower()
        if choice_door=="red":
            print("Burned by fire. Game Over!")
        elif choice_door=="blue":
            print("Eaten by beasts. Game Over!")
        elif choice_door=="yellow":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")




student_scores = input("Inout a list of student scores ").split()
highest_score=student_scores[0]
for scores in range (0,len(student_scores)):
    if highest_score<student_scores[scores]:
        highest_score=student_scores[scores]

print(highest_score) 


for i in range(1,100):
    if i%3==0 and i%5==0:
        print(f"{i} FizzBuzz")
    elif i%3==0:
        print(f"{i} Fizz")
    elif i%5==0:
        print(f"{i} Buzz")



import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = "".join(random.choices(letters,k=nr_letters)+random.choices(numbers,k=nr_numbers)+random.choices(symbols,k=nr_symbols))





print(password)
rand_num = random.randint(0,2)
if rand_num == 0:
    password = "".join(
        random.choices(letters, k=nr_letters) + random.choices(numbers, k=nr_numbers) + random.choices(symbols,
                                                                                                       k=nr_symbols))
print (rand_num)


import random
word_list = ["ardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


display = []
for _ in range(len(chosen_word)):
    display+="_"
print(display)

guess = input("Word has been choosed! Guess a letter.\n").lower()

def init():
    display = []
    for _ in range(len(chosen_word)):
        display += "_"
    print(display)
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

def checking_blank():
    init()
    for i in display:
        while i=="_":
            init()
            break



checking_blank()
print("Welcome to my quiz game! ")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("OKAY! lets play ")

answer = input("What does CPU stands for? ")
if answer == "Central processing unit":
    print('Hurray! Correct')
else:
    print("Oho! Incorrect")

answer = input("What is the capital of Pakistan?")
if answer == "Islamabad":
    print("superb! you are amazing")
else:
    print("sorry! please try again")

answer = input("Are you 21 years old?")
if answer == "yes":
    print("Congrats you are near to your success")
else:
    print("ok good you have to work hard")


answer = input("What does GPU stands for? ")
if answer == "Graphical processing unit":
    print('Keep it up! Correct')
else:
    print("Oho! Incorrect! Don't lose hope try again")

answer = input("What does API stands for? ")
if answer == "Application programming interface":
    print('Nice! Correct')
else:
    print("sad! Incorrect")

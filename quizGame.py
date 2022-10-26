print("Welcome to Marcia, Shannon & Paddy's quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does IS stand for? Use the reaction 'thumbs up' for 'information systems' or 'heart' for 'information software' ")
if answer.lower() == "information systems":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does BI stand for? 'thumbs up' for 'business information' or 'heart' for 'business intelligence' ")
if answer.lower() == "business intelligence":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" What does the 'O' stand for in the CMS POPE values? 'thumbs up' for 'operationl excellence' or 'heart' for 'occasionally exceeding' ")
if answer.lower() == "operational excellence":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What year was CMS founded? 'thumbs up' for '1996' or 'heart' for '1988' ")
if answer.lower() == "1988":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

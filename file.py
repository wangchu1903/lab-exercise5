
labEx = int(input("Enter lab ex"))
questions = int(input("number of questions"))

for i in range(questions + 1):
    f = open("Lab_" + str(labEx) + "_Question_"+ str(i + 1) + ".py", "w")


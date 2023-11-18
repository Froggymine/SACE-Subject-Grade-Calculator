import math

# ---------------------
#       Constants
gradenums = {
    "E-": 1,
    "E" : 2,
    "E+": 3,
    "D-": 4,
    "D" : 5,
    "D+": 6,
    "C-": 7,
    "C" : 8,
    "C+": 9,
    "B-": 10,
    "B" : 11,
    "B+": 12,
    "A-": 13,
    "A" : 14,
    "A+": 15
}

grades_list = ["E-","E","E+","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]

subjects = {
    "physics": [["SATs", "Investigation Folios", "Exam"],[0.4, 0.3, 0.3]],
    "math methods": [["SATs", "Mathmatical Investigation", "Exam"],[0.5, 0.2, 0.3]],
}

# -------------------
#        Input
print("                                              ")
print("                                              ")
print("     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄    ")
print("    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌   ")
print("    ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀    ")
print("    ▐░▌          ▐░▌          ▐░▌             ")
print("    ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌             ")
print("    ▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌▐░▌             ")
print("     ▀▀▀▀▀▀▀▀▀█░▌▐░▌ ▀▀▀▀▀▀█░▌▐░▌             ")
print("              ▐░▌▐░▌       ▐░▌▐░▌             ")
print("     ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄    ")
print("    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌   ")
print("     ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀    ")
print("                                              ")
print("             SACE Grade Calculator            ")
print("                                              ")

print("Avalible Subjects: " + ", ".join(list(subjects.keys())))
selected_subject = subjects[input("Enter Subject: ")]

grades1_weight = selected_subject[1][0]
grades2_weight = selected_subject[1][1]
grades3_weight = selected_subject[1][2]

print("\n--------------------------------------------")

print("\nFor the following, input grades on one line")
print("seperated with a space like such:\n")
print("    A+ E B- B C")

print("\n--------------------------------------------")

print("\nGrade(s) for type: " + selected_subject[0][0])
grades1 = input("Enter: ").split()
if selected_subject[0][1] != "N/A":
    print("\nGrade(s) for type: " + selected_subject[0][1])
    grades2 = input("Enter: ").split()
if selected_subject[0][2] != "N/A":
    print("\nGrade(s) for type: " + selected_subject[0][2])
    grades3 = input("Enter: ").split()

# -------------------------
#       Calculations

grades1_num = 0
for i in grades1:
    grades1_num += gradenums[i]
grades1_num = grades1_num / len(grades1)

grades2_num = 0
for i in grades2:
    grades2_num += gradenums[i]
grades2_num = grades2_num / len(grades2)

grades3_num = 0
for i in grades3:
    grades3_num += gradenums[i]
grades3_num = grades3_num / len(grades3)

grades1_num *= grades1_weight
grades2_num *= grades2_weight
grades3_num *= grades3_weight

final_grade = grades1_num + grades2_num + grades3_num

# I've tried so much but there is always stuff like 7.800000000000001 whyyyyyyyyy

print("\n--------------------------------------------")
print("--------------- Calculations ---------------\n")

print("Raw calculated score out of 15: " + str(round(final_grade, 2)) + "/15")

print("Raw score out of 20:            " + str(round((final_grade/15)*20)) + "/20")

print("Score out of 100:               " + str(round((final_grade/15)*100)) + "/100")

print("Final average grade:            " + str(list(gradenums.keys())[list(gradenums.values()).index(round(final_grade))]) + "\n")

input("\nPress ENTER to close")

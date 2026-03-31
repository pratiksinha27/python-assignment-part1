# Part 1: Python Basics & Control Flow
# Theme: Student Grade Tracker

# ============================================================
# Task 1 — Data Parsing & Profile Cleaning
# ============================================================

# this is our raw student data as given
# names have extra spaces and wrong letter format
# roll numbers are stored as string
# the marks are in string form instead of list
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# we will create a new list to store cleaned student data
cleaned_students = []

# now we go through each student one by one
for student in raw_students:

    # first we take the name and remove extra spaces from left and right
    name = student["name"]
    name = name.strip()

    # now we convert the name into proper format
    # so first letter becomes capital and rest small
    name = name.title()

    # roll number is in string form, so we convert it into integer
    roll = student["roll"]
    roll = int(roll)

    # marks are given as one string, so we split it using comma
    marks_string = student["marks_str"]
    parts = marks_string.split(", ")

    # we create empty list to store marks as numbers
    marks = []

    # now we convert each part into integer and store in list
    for p in parts:
        p = p.strip()          # remove space around number
        num = int(p)           # convert string to integer
        marks.append(num)      # add number into list

    # now we create a new dictionary to store cleaned data
    new_student = {}
    new_student["name"] = name
    new_student["roll"] = roll
    new_student["marks"] = marks

    # we add this cleaned student into list
    cleaned_students.append(new_student)

    # now we check if the name is valid
    # valid means each word has only alphabets (no numbers or symbols)
    words = name.split()
    valid = True

    for w in words:
        if not w.isalpha():
            valid = False

    # print whether the name is valid or not
    if valid:
        print("✓ Valid name", name)
    else:
        print("✗ Invalid name", name)

    # print student profile card using f-string formatting
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")


# now we find student with roll number 103 and print name in upper case and lower case
for student in cleaned_students:
    if student["roll"] == 103:
        print("Upper case:", student["name"].upper())
        print("Lower case:", student["name"].lower())


# ============================================================
# Task 2 — Marks Analysis Using Loops & Conditionals
# ============================================================

# here we have subjects and marks of one student as given
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# print heading
print("\nMarks report for", student_name)

# use for loop to go through each subject and print marks with grade
for i in range(len(subjects)):
    subject = subjects[i]
    mark = marks[i]

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(subject, ":", mark, "=>", grade)


# now we calculate total marks by adding each value
total = 0
for m in marks:
    total = total + m

# calculate average by dividing total by number of subjects
average = total / len(marks)
average = round(average, 2)

print("Total marks:", total)
print("Average marks:", average)


# now we find highest marks manually
highest = marks[0]
for m in marks:
    if m > highest:
        highest = m

# now we find position (index) of highest marks
index_high = 0
i = 0
while i < len(marks):
    if marks[i] == highest:
        index_high = i
    i = i + 1

print("Highest subject:", subjects[index_high], highest)


# now we find lowest marks manually
lowest = marks[0]
for m in marks:
    if m < lowest:
        lowest = m

# find position (index) of lowest marks
index_low = 0
i = 0
while i < len(marks):
    if marks[i] == lowest:
        index_low = i
    i = i + 1

print("Lowest subject:", subjects[index_low], lowest)


# now we take input from user to add new subjects
# loop will keep running until user types "done"
print("\nAdd new subjects (type done to stop)")

count = 0

while True:
    sub = input("Enter subject: ")

    if sub == "done":
        break

    mark_input = input("Enter marks: ")

    # here we check if input is valid number manually
    valid_number = True

    for ch in mark_input:
        if ch < '0' or ch > '9':
            valid_number = False

    if valid_number == False:
        print("Invalid input, please enter only numbers")
        continue

    mark_value = int(mark_input)

    # check if marks are in valid range
    if mark_value < 0 or mark_value > 100:
        print("Marks should be between 0 and 100")
        continue

    # if everything is correct, we add data into list
    subjects.append(sub)
    marks.append(mark_value)
    count = count + 1

    print("Subject added successfully")

print("Total new subjects:", count)

# calculate new average after adding subjects
new_total = 0
for m in marks:
    new_total = new_total + m

new_avg = new_total / len(marks)
new_avg = round(new_avg, 2)

print("Updated average:", new_avg)


# ============================================================
# Task 3 — Class Performance Summary
# ============================================================

# here we have marks of multiple students
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85]),
]

print("\nName              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0

top_name = ""
top_avg = 0

total_avg = 0

# go through each student and calculate average and result
for data in class_data:

    name = data[0]
    marks = data[1]

    # calculate total marks
    total = 0
    for m in marks:
        total = total + m

    # calculate average
    avg = total / len(marks)
    avg = round(avg, 2)

    # decide pass or fail
    if avg >= 60:
        status = "Pass"
        pass_count = pass_count + 1
    else:
        status = "Fail"
        fail_count = fail_count + 1

    print(name.ljust(18), "|", f"{avg:.2f}".ljust(6), "|", status)

    # check if this student is topper
    if avg > top_avg:
        top_avg = avg
        top_name = name

    total_avg = total_avg + avg


# calculate class average
class_average = total_avg / len(class_data)
class_average = round(class_average, 2)

print("Passed:", pass_count)
print("Failed:", fail_count)
print("Topper:", top_name, top_avg)
print("Class Average:", class_average)


# ============================================================
# Task 4 — String Manipulation Utility
# ============================================================

# here we have an essay with extra spaces as given 
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# remove spaces and store as clean_essay (used for all steps)
clean_essay = essay.strip()
print("Clean Essay:", clean_essay)

# convert text into title case
title_case = clean_essay.title()
print("Title Case:", title_case)

# count how many times word 'python' appears
count = clean_essay.count("python")
print("Python count:", count)

# replace 'python' with 'Python 🐍'
replaced = clean_essay.replace("python", "Python 🐍")
print("Replaced:", replaced)

# split essay into sentences
sentences = clean_essay.split(". ")
print("Sentences:", sentences)

# print each sentence with numbering
num = 1
for s in sentences:
    if not s.endswith("."):
        s = s + "."
    print(num, "-", s)
    num = num + 1
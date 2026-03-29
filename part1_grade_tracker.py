# Part 1: Python Basics & Control Flow
# Theme: Student Grade Tracker

# ============================================================
# Task 1 — Data Parsing & Profile Cleaning
# ============================================================

# this is our raw student data. The names are not properly formatted and the marks are in string form.
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# list to store cleaned student data
cleaned_students = []


for s in raw_students:

    # remove extra spaces from name and make it title case
    name = s["name"].strip().title()

    # roll is string so convert it to int
    roll = int(s["roll"])

    # marks are in a string, so split and convert each value to int
    marks = []
    parts = s["marks_str"].split(", ")

    for p in parts:
        marks.append(int(p))

    # store cleaned data in a dictionary
    cleaned = {"name": name, "roll": roll, "marks": marks}
    cleaned_students.append(cleaned)
    
    # check if the name is valid, each word should contain only alphabets
    words = name.split()
    valid = True

    for w in words:
        if not w.isalpha():
            valid = False

    if valid:
        print(f"✓ Valid name : {name}")
    else:
        print(f"✗ Invalid name : {name}")

    # print profile card using f-string
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

# find roll 103 and print name in upper and lower case
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nUpper case : {s['name'].upper()}")
        print(f"Lower case : {s['name'].lower()}")
print("\n========== Task 1 Completed ==========\n")


# ============================================================
# Task 2 — Marks Analysis Using Loops & Conditionals
# ============================================================

# given data for task 2
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# print heading for marks report
print(f"\nMarks report for {student_name}")
print("-" * 35)

# loop through each subject and assign grade based on marks
for i in range(len(subjects)):
    m = marks[i]

    # checking marks range and giving grade
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subjects[i]} : {m} => {grade}")

# calculate total and average
total = sum(marks)
avg = round(total / len(marks), 2)

print(f"\nTotal   : {total}")
print(f"Average : {avg}")

# find highest and lowest subject
high = max(marks)
low = min(marks)

print(f"Highest : {subjects[marks.index(high)]} ({high})")
print(f"Lowest  : {subjects[marks.index(low)]} ({low})")

# while loop to add new subjects
print("\nAdd new subjects, type done to stop")

new_sub = []

while True:
    sub = input("Subject name: ").strip()

    if sub.lower() == "done":
        break

    mark_input = input(f"Marks for {sub} (0-100): ").strip()

    # check if input is a number
    if not mark_input.isdigit():
        print("please enter a valid number")
        continue

    mark_val = int(mark_input)

    # marks should be between 0 and 100
    if mark_val < 0 or mark_val > 100:
        print("marks should be between 0 and 100")
        continue

    # adding new subject and marks to original list
    subjects.append(sub)
    marks.append(mark_val)
    new_sub.append(sub)

    print(f"added {sub}")

print(f"\nTotal new subjects added : {len(new_sub)}")

# calculate updated average using updated marks list
updated_avg = round(sum(marks) / len(marks), 2)
print(f"Updated average : {updated_avg}")
print("\n========== Task 2 Completed ==========\n")


# ============================================================
# Task 3 — Class Performance Summary
# ============================================================

# given data for task 3
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# print table heading
print("Name | Average | Status")
print("-" * 30)

# counters for pass and fail
passed = 0
failed = 0

# variables to track topper
topper = ""
top_avg = 0

# to store total of averages for class average
total = 0

# loop through each student
for name, marks in class_data:
    
    # calculate average marks
    avg = sum(marks) / len(marks)
    avg = round(avg, 2)
    
    # check pass or fail
    if avg >= 60:
        status = "Pass"
        passed += 1
    else:
        status = "Fail"
        failed += 1

    # print student data
    print(name, "|", avg, "|", status)

    # check for topper (highest average)
    if avg > top_avg:
        top_avg = avg
        topper = name

    # add to total for class average
    total += avg

# calculate class average
class_avg = round(total / len(class_data), 2)

# print final summary
print("\nPassed:", passed)
print("Failed:", failed)
print("Topper:", topper, top_avg)
print("Class Average:", class_avg)
print("\n========== Task 3 Completed ==========\n")


# ============================================================
# Task 4 - String Manipulation Utility
# ============================================================

# given essay (with extra spaces at start and end)
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# remove extra spaces from both sides
clean_essay = essay.strip()
print("\nStep 1 - Stripped:")
print(clean_essay)

# convert sentence into title case
title_case = clean_essay.title()
print("\nStep 2 - Title Case:")
print(title_case)

# count how many times 'python' appears
count = clean_essay.count("python")
print("\nStep 3 - Count of python:", count)

# replace 'python' with 'Python 🐍'
replaced = clean_essay.replace("python", "Python 🐍")
print("\nStep 4 - After Replacement:")
print(replaced)

# split essay into sentences using ". "
sentences = clean_essay.split(". ")
print("\nStep 5 - Sentences List:")
print(sentences)

# print each sentence with numbering
print("\nStep 6 - Numbered Sentences:")
i = 1
for sentence in sentences:
    
    # add full stop if missing at end
    if not sentence.endswith("."):
        sentence = sentence + "."
    
    print(i, "-", sentence)
    i += 1

# task completed message
print("\n========== Task 4 Completed ==========\n")
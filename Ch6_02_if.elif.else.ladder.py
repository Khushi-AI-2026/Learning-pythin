# If-Elif-Else Ladder Explanation and Examples

# ===== CONCEPT =====
# if-elif-else is a decision-making structure:
# - if: Check first condition
# - elif: Check second condition if first is False
# - else: Execute if all conditions are False
# Only ONE block executes - whichever condition is True first


# ===== EXAMPLE 1: Student Grades =====
print("=== Example 1: Student Grades ===")
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F (Fail)")


# ===== EXAMPLE 2: Age Categories =====
print("\n=== Example 2: Age Categories ===")
age = 25

if age < 13:
    print("Category: Child")
elif age < 18:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")


# ===== EXAMPLE 3: Traffic Light System =====
print("\n=== Example 3: Traffic Light ===")
color = "yellow"

if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Get Ready!")
elif color == "green":
    print("Go!")
else:
    print("Invalid color")


# ===== EXAMPLE 4: Temperature Advice =====
print("\n=== Example 4: Temperature Advice ===")
temp = 15

if temp > 30:
    print("Very hot! Drink cold water")
elif temp > 20:
    print("Warm weather")
elif temp > 10:
    print("Cold! Wear a sweater")
else:
    print("Very cold!")


# ===== EXAMPLE 5: Days of the Week =====
print("\n=== Example 5: Days of the Week ===")
day = 5

if day == 1:
    print("Monday - Work starts")
elif day == 2:
    print("Tuesday - Still working")
elif day == 3:
    print("Wednesday - Mid week")
elif day == 4:
    print("Thursday - Almost weekend")
elif day == 5:
    print("Friday - Last work day")
elif day == 6:
    print("Saturday - Weekend!")
elif day == 7:
    print("Sunday - Rest day")
else:
    print("Invalid day number")


# ===== EXAMPLE 6: Number Classification =====
print("\n=== Example 6: Number Classification ===")
num = -5

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


# ===== EXAMPLE 7: Percentage Score =====
print("\n=== Example 7: Percentage Score ===")
percentage = 75

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good!")
elif percentage >= 40:
    print("Pass!")
else:
    print("Fail!")

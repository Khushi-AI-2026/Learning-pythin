# Multiple If Statements - Python

# ============================================================
# 1. MULTIPLE SEPARATE IF STATEMENTS
# ============================================================
print("=== 1. Multiple Separate If Statements ===")
print("Each if statement is checked independently\n")

age = 20
score = 75
income = 50000

# Each if is separate, all will be checked
if age >= 18:
    print("✓ You are eligible to vote")

if score >= 60:
    print("✓ You passed the exam")

if income > 40000:
    print("✓ Your income is good")


# ============================================================
# 2. IF-ELIF-ELSE (Mutually Exclusive)
# ============================================================
print("\n=== 2. If-Elif-Else (Only one will execute) ===\n")

grade = 85

if grade >= 90:
    print("Grade: A+")
elif grade >= 80:
    print("Grade: A")
elif grade >= 70:
    print("Grade: B")
elif grade >= 60:
    print("Grade: C")
else:
    print("Grade: F (Fail)")


# ============================================================
# 3. MULTIPLE IF WITH AND/OR CONDITIONS
# ============================================================
print("\n=== 3. Multiple Conditions (AND/OR) ===\n")

temperature = 28
humidity = 60

if temperature > 25 and humidity > 50:
    print("🌞 It's hot and humid weather")

if temperature < 15 or humidity < 30:
    print("❄️ It's cold or dry weather")

if temperature >= 20 and temperature <= 30:
    print("😊 The weather is pleasant")


# ============================================================
# 4. NESTED IF STATEMENTS (If inside If)
# ============================================================
print("\n=== 4. Nested If Statements (If inside If) ===\n")

student_age = 22
scholarship_eligible = True

if student_age >= 18:
    print("You are an adult")
    if scholarship_eligible:
        print("✓ You are eligible for scholarship")
    else:
        print("✗ You are not eligible for scholarship")


# ============================================================
# 5. REAL WORLD EXAMPLE - ATM WITHDRAWAL
# ============================================================
print("\n=== 5. Real World Example: ATM Machine ===\n")

account_balance = 5000
withdrawal_amount = 1500
pin_correct = True

if pin_correct:
    print("✓ PIN is correct")
    if withdrawal_amount <= account_balance:
        print(f"✓ You received: ${withdrawal_amount}")
        account_balance -= withdrawal_amount
        print(f"Remaining balance: ${account_balance}")
    else:
        print("✗ Insufficient balance")
else:
    print("✗ PIN is incorrect!")


# ============================================================
# 6. MULTIPLE IF - STUDENT ELIGIBILITY CHECK
# ============================================================
print("\n=== 6. Student Eligibility Check (All must pass) ===\n")

age = 25
gpa = 3.5
attendance = 85
work_experience = 2

print("Student Information:")
print(f"Age: {age}, GPA: {gpa}, Attendance: {attendance}%, Experience: {work_experience} years\n")

if age >= 18:
    print("✓ Age requirement met")

if gpa >= 3.0:
    print("✓ GPA requirement met")

if attendance >= 75:
    print("✓ Attendance requirement met")

if work_experience >= 2:
    print("✓ Experience requirement met")

# Final decision
if age >= 18 and gpa >= 3.0 and attendance >= 75 and work_experience >= 2:
    print("\n🎉 Congratulations! You meet all requirements! Admission approved!")
else:
    print("\n❌ Some requirements are not met")


# ============================================================
# 7. BONUS - MULTIPLE IF USING LOOP
# ============================================================
print("\n=== 7. Multiple Checks Using Loop ===\n")

subjects = {'Math': 85, 'Science': 92, 'English': 78}

print("Performance by Subject:")
for subject, marks in subjects.items():
    if marks >= 90:
        print(f"{subject}: Excellent! 🌟")
    if marks >= 80 and marks < 90:
        print(f"{subject}: Good! 👍")
    if marks < 80:
        print(f"{subject}: Need improvement 📚")


# ============================================================
# 8. KEY DIFFERENCES - IMPORTANT CONCEPTS
# ============================================================
print("\n=== 8. Key Differences ===\n")

print("Multiple Separate IF:")
print("- All conditions are checked")
print("- All matching blocks will execute")
print("- Use when checking independent conditions\n")

print("IF-ELIF-ELSE:")
print("- Only ONE block will execute")
print("- Checks conditions in order")
print("- Use when checking related conditions\n")

print("NESTED IF:")
print("- If inside another if")
print("- Inner if only executes if outer if is true")
print("- Use for dependent conditions")

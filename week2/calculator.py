"""
Project: Comprehensive Grade Calculator
Author: Trisha Dabral
Description:
This program collects marks of multiple students,
calculates grades with comments, stores results,
displays statistics, and allows searching & saving data.
"""

# -------------------- FUNCTIONS --------------------

def calculate_grade(avg):
    """Determine grade based on average marks"""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def grade_comment(grade):
    """Return comment based on grade"""
    if grade == "A":
        return "Excellent performance!"
    elif grade == "B":
        return "Very good job!"
    elif grade == "C":
        return "Good, but can improve."
    elif grade == "D":
        return "Needs more practice."
    else:
        return "Fail. Work harder next time."


def get_valid_marks(subject):
    """Validate marks input (0–100)"""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Enter numeric value.")


# -------------------- MAIN PROGRAM --------------------

students = []
results = []

# Step 3: Number of students
while True:
    try:
        n = int(input("Enter number of students: "))
        if n > 0:
            break
        else:
            print("❌ Number must be positive.")
    except ValueError:
        print("❌ Enter a valid number.")

# Step 4 & 5: Collect and process data
for i in range(n):
    print(f"\n--- Student {i + 1} ---")
    name = input("Enter student name: ")

    m1 = get_valid_marks("Subject 1")
    m2 = get_valid_marks("Subject 2")
    m3 = get_valid_marks("Subject 3")

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)
    comment = grade_comment(grade)

    students.append(name)
    results.append([name, m1, m2, m3, avg, grade, comment])

# -------------------- STATISTICS --------------------

averages = [student[4] for student in results]
class_avg = sum(averages) / len(averages)
highest = max(averages)
lowest = min(averages)

# -------------------- DISPLAY RESULTS --------------------

print("\n📊 STUDENT RESULTS")
print("-" * 90)
print(f"{'Name':<15}{'Sub1':<8}{'Sub2':<8}{'Sub3':<8}{'Avg':<8}{'Grade':<8}{'Comment'}")
print("-" * 90)

for r in results:
    print(f"{r[0]:<15}{r[1]:<8.1f}{r[2]:<8.1f}{r[3]:<8.1f}{r[4]:<8.2f}{r[5]:<8}{r[6]}")

print("-" * 90)
print(f"Class Average: {class_avg:.2f}")
print(f"Highest Average: {highest:.2f}")
print(f"Lowest Average: {lowest:.2f}")

# -------------------- SEARCH FEATURE --------------------

search = input("\n🔍 Search student name (or press Enter to skip): ").strip()
if search:
    found = False
    for r in results:
        if r[0].lower() == search.lower():
            print("\nStudent Found:")
            print(r)
            found = True
            break
    if not found:
        print("❌ Student not found.")

# -------------------- SAVE TO FILE --------------------

save = input("\n💾 Save results to file? (y/n): ").lower()
if save == "y":
    with open("results.txt", "w") as file:
        for r in results:
            file.write(str(r) + "\n")
    print("✅ Results saved successfully.")

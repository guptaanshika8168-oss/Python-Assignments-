import csv
import json

# Store student details
students = [
    {"Roll Number": 101, "Name": "Rahul", "Branch": "CSE", "Marks": [85, 78, 92, 88, 90]},
    {"Roll Number": 102, "Name": "Priya", "Branch": "ECE", "Marks": [75, 82, 79, 85, 80]},
    {"Roll Number": 103, "Name": "Amit", "Branch": "IT", "Marks": [65, 70, 68, 72, 75]}
]

# Create CSV file
csv_file = "students.csv"

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Roll Number", "Name", "Branch",
        "Mark1", "Mark2", "Mark3", "Mark4", "Mark5"
    ])

    for student in students:
        writer.writerow([
            student["Roll Number"],
            student["Name"],
            student["Branch"],
            *student["Marks"]
        ])

print("Student details stored in students.csv")


# Read CSV file
processed_students = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        # Get marks
        marks = [
            int(row["Mark1"]),
            int(row["Mark2"]),
            int(row["Mark3"]),
            int(row["Mark4"]),
            int(row["Mark5"])
        ]

        # Calculate total
        total = sum(marks)

        # Calculate percentage
        percentage = total / len(marks)

        # Calculate grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        # Create processed record
        student = {
            "Roll Number": int(row["Roll Number"]),
            "Name": row["Name"],
            "Branch": row["Branch"],
            "Marks": marks,
            "Total Marks": total,
            "Percentage": round(percentage, 2),
            "Grade": grade
        }

        processed_students.append(student)


# Store processed records in JSON
json_file = "students_processed.json"

with open(json_file, "w") as file:
    json.dump(processed_students, file, indent=4)

print("Processed records stored in students_processed.json")


# Display results
print("\nStudent Records:")

for student in processed_students:
    print("--------------------------------")
    print("Roll Number:", student["Roll Number"])
    print("Name:", student["Name"])
    print("Branch:", student["Branch"])
    print("Marks:", student["Marks"])
    print("Total Marks:", student["Total Marks"])
    print("Percentage:", student["Percentage"], "%")
    print("Grade:", student["Grade"])
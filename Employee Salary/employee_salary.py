import csv

with open("Employee Salary/employee.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        monthly_salary = float(row["Monthly Salary"])

        annual_salary = monthly_salary * 12

        print("--------------------------------")
        print("Employee ID:", row["Employee ID"])
        print("Name:", row["Name"])
        print("Department:", row["Department"])
        print("Monthly Salary: ₹", monthly_salary)
        print("Annual Salary: ₹", annual_salary)

        if monthly_salary > 50000:
            print("Employee earns above ₹50,000 per month")
#comprehenssion - Create lists using a single line of code instead of loops

sqs = [x ** 2 for x in range(1,6)]
print(sqs)

#with the condition
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# Dict comphersion - increase by 10%

salary = {"a" : 50000, "b" : 60000, "c" : 70000}
updated_salary = {k : v + 0.1 * v for k, v in salary.items()}
print(updated_salary)


employees = {
    "Harsha" : "Active",
    "Amit" : "Inactive",
    "Hari" : "Active"
}
active_employees = {k : v for k , v in employees.items() if v == "Active"}
print(active_employees)


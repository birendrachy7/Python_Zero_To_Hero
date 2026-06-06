import csv

# Writing a CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Bibek', '23', 'DNG'],
    ['Biru', '21', 'KTM']
]

with open('people.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Reading using csv.reader
with open('people.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)
    print(f"Header: {header}")

    for row in csv_reader:
        print(row)

print("\n--------------------------------------\n")

# Reading using DictReader
students = []

with open('people.csv', 'r', newline='') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        students.append(row)

print(f"Students: {students}")

# Writing using DictWriter
with open('student_output.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

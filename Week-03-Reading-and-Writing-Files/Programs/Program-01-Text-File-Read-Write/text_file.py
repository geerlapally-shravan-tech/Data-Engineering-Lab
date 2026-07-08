# Program: Reading and Writing Text Files

file = open("student.txt", "w")

file.write("Student Name : Rahul\n")
file.write("Roll Number : 101\n")
file.write("Department  : CSE\n")
file.write("College     : ABC Engineering College\n")

file.close()

print("Data has been written successfully.\n")

file = open("student.txt", "r")

content = file.read()

print("Contents of student.txt")
print("------------------------")
print(content)

file.close()

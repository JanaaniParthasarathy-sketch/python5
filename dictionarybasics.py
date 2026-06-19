# Dictionary Basics

student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print("Student Details:")
print(student)

# Update value
student["age"] = 21

# Add new key-value pair
student["city"] = "New York"

print("\nUpdated Dictionary:")
print(student)

# Access values
print("\nName:", student["name"])

# Iterate through dictionary
print("\nDictionary Contents:")
for key, value in student.items():
    print(key, ":", value)

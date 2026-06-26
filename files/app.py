# ============================
# PYTHON FILE HANDLING
# ============================

# ----------------------------
# File Modes
# ----------------------------
# "r" -> Read (file must exist)
# "w" -> Write (overwrites file or creates a new one)
# "a" -> Append (adds data to the end of the file)
# "x" -> Create (creates a new file, throws error if it already exists)


# ============================
# READING FILES
# ============================

employee_file = open("employees.txt", "r")

# Check if file is readable
print(employee_file.readable())       # True

# Read entire file
# print(employee_file.read())

# Read one line at a time
# print(employee_file.readline())
# print(employee_file.readline())

# Read all lines (returns a list)
# print(employee_file.readlines())

# Loop through each line
for employee in employee_file.readlines():
    print(employee)

employee_file.close()


# ============================
# APPENDING TO A FILE
# ============================

employee_file = open("employees.txt", "a")

# Adds new text at the end of the file
employee_file.write("\nKelly - Customer Service")

employee_file.close()


# ============================
# WRITING / OVERWRITING A FILE
# ============================

employee_file = open("index.html", "w")

# Creates the file if it doesn't exist
# Overwrites the file if it already exists
employee_file.write("<p>This is a webpage!</p>")

employee_file.close()


# ============================
# MODERN WAY (Recommended)
# ============================

# Automatically closes the file
with open("employees.txt", "r") as employee_file:
    print(employee_file.read())
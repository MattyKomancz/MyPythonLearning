# Formatting Strings

file_number = 7
file_name = "import_july.csv"
file_size = 1024
message = f"Step {file_number}: processing {file_name} of size {file_size}"
print(message)

file_number = 8
file_name = "import august.csv"
file_size = 2048
message = f"Step {file_number}: processing {file_name} of size {file_size}"
print(message)

message = "step %d: procesing %s of size%d"
print(message % (file_number, file_name, file_size))

file_number = 9
file_name = "import september.csv"
file_size = 512
print(message % (file_number, file_name, file_size))

message = "Step {0}: processing {1} of size {2}"
print(message.format(file_number, file_name, file_size))

file_number = 10
file_name = "import october.csv"
file_size = 4096
print(message.format(file_number, file_name, file_size))

# Formatting options

name = "Mario"
print(f"|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")
print(f"|{name:*^10}|")

x = 3.14159265
print(f"{x:.2f}")
print(f"{x:10.3f}")

n = 1234567
print(f"{n:10d}")
print(f"{n:,}")

ratio = 0.1234
print(f"{ratio:.2%}")
print(f"{ratio:.0%}")

n = 255
print(f"{n:b}")
print(f"{n:o}")
print(f"{n:x}")
print(f"{n:X}")

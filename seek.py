file = open("example.txt", "w+")

file.write("Hello siva\n")
file.write("Welcome to Python File .\n")

file.flush()
print("Data flushed to file.")

file.seek(0)
print("Cursor moved to beginning.")

position = file.tell()
print("Current file position:", position)

data = file.read(5)
print("First 5 characters:", data)
print("Position after reading 5 characters:", file.tell())

file.seek(6, 0) 
print("Cursor moved 6 bytes forward from current position.")
print("Current position:", file.tell())

file.seek(0, 2)
print("Cursor moved to end of file.")
print("Final position:", file.tell())
file.close()

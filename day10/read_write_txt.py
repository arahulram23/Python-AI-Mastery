with open("file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Goodbye!\n")
    file.write("This is the last line.\n")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

with open("file.txt", "a") as file:
    file.write("Appending a new line.\n")
    file.write("This is another appended line.\n")

with open("file.txt", "r") as file:
    content = file.readlines()
    print(content)
    
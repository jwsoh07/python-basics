# Open a file in write mode ('w)
with open("example.txt", "w") as file:
  file.write("Hello, world!\n")
  file.write("This is a file handling exercise.\n")

# Open a file in append mode ('a')
with open("example.txt", "a") as file:
    file.write("\nAppending some text here!")  # \n ensures it goes to a new line

print("File written successfully!")

# Read contents from the file in read mode ('r')
with open("example.txt", "r") as file:
    content = file.read()  # Read the entire file content
    print("File contents:\n", content)

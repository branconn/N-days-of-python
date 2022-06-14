# Day 24: File I/O

# NOTES
# using "with" you do not have to close the file
# mode=w makes it writeable
# mode=a makes it appendable
# mode=r makes it readable
# !

# majority of today is altering the snake game (day 20)

with open("my_file.txt", mode="w") as file:
    file.write("banana")

# File paths:
#   at the very root is the root folder, represented as /, usually C: drive
#   /first_folder/second_folder/doc.ext < absolute file path starts from root
#   ./doc.ext < relative file path starts from working directory
#   ../upper_folder.doc.ext < go up one folder
#   ./ usually not necessary at all
#   !





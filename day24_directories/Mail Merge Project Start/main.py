# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
REPLACED = "[name]"
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names_list = names_file.readlines()
with open("./Input/Letters/starting_letter.txt", mode="r") as template_file:
    template = template_file.read()

for name in names_list:
    name = name.strip()
    with open(f"./Output/ReadyToSend.{name}Letter.txt", mode="w") as working_file:
        contents = template.replace(REPLACED, name)
        working_file.write(contents)

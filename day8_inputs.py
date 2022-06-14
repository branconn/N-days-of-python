# NOTES & CHALLENGES
# parameter is the name of the variable, argument is it's value
# these are positional arguments, order they are listed matter
# there are keyword arguments like name = "Brandon" to disassociate from position
def banana_counter(num_bananas):
    # counts the number of bananas you have given the number of bananas
    for i in range(1, num_bananas):
        if i == 1:
            print(f"{i} banana")
        else:
            print(f"{i} bananas")
    print(num_bananas)


def greet_with_name(name):
    print(f"Hello {name}")


def greet_with(name, location):
    print(f"Hello {name}, what is it like in {location}?")


# greet_with("Brandon", "Atlanta")
# banana_counter(4)

# Area calculation exercise
# calculate the number of paint cans needed based on LxW inputs
def paint_needed(length, width):
    coverage = 5  # m^2
    cans = length * width / coverage
    if cans % 1 != 0:
        cans += 1
    cans = int(cans)
    print(f"You need {cans} cans of paint")


# paint_needed(3, 9)

# Prime number checker
def primer(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        print("She's a prime!")
    else:
        print("She's divisible, bro")

# def primer(num_cap):
#     primes = []
#     for i in range(2,numCap):
#
#

# primer(181)

# PROJECT: Caesar's Cipher
# shift each letter by a predetermined amount
import asciiArt


def encryptor(direction, message, offset):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', ' ', '!', '?', ',', '.']
    offset = int(offset)
    message = message.lower()
    new_message = ""
    sign = 1
    if direction == "decode":
        sign = -1
    for i in range(len(message)):
        if message[i] in letters:
            where_is_it = letters.index(message[i]) + offset * sign
            if abs(where_is_it) >= len(letters):
                where_is_it = where_is_it % len(letters)
            new_letter = letters[where_is_it]
            new_message += new_letter
        else:
            new_message += message[i]
    print(f"Here is your encrypted message: {new_message}")


print(asciiArt.homer)
cont = True
while cont:
    encryptOrNo = input("Do you want to 'encode' or 'decode'? ")
    note = input("Paste your message (encrypted or to-be encrypted): ")
    shift = int(input("What is your shift amount? "))
    encryptor(encryptOrNo, note, shift)
    answer = input("Do you want to continue? [y/n]: ")
    if answer != "y":
        cont = False

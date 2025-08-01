specials = "@#$%^&*!~"
n = input()
result = []
skip = False

for i in range(len(n)):
    if skip:
        skip = False
        continue
    if n[i] in specials:
        skip = True  
        continue
    result.append(n[i])

print(''.join(result))

# This code removes special characters from the input string and skips the next character after each special character.
# It uses a list to collect the characters that are not special and not immediately following a special character.
# Finally, it prints the cleaned string without special characters and the characters that follow them.

#this code uses a flag to skip the next character after a special character is found because deletion is not allowed for stings in Python.
# The result is printed as a single string without spaces.
import sys

lines = sys.stdin.readlines()

origTokens = ""
origSent = ""

tokTokens = ""
tokSent = ""

for line in lines:
    if line[0] == '#':
        continue
    elif line == "\n":
        origTokens = origTokens + origSent + "\n"
        origSent = ""
        tokTokens = tokTokens + tokSent + "\n"
        tokSent = ""
    else:
        sep = line.split()
        token = sep[1]
        origSent += token
        tokSent = tokSent + token + " "

try:
    with open('original.txt', 'w') as file:
        file.write(origTokens)
except FileNotFoundError:
    print("No file found")

try:
    with open('tokenised.txt', 'w') as file:
        file.write(tokTokens)
except FileNotFoundError:
    print("No file found")


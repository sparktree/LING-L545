tokTrain = open("tokenised.train.txt", 'r')

lines = tokTrain.readlines()
print(lines)

dict = open("dictionary.txt", 'w+')
dictTokens = []

for line in lines:
        tokens = line.split()
        for token in tokens:
              if token not in dictTokens:
                   dictTokens.append(token)
                   dict.write(token + '\n')


"""
try:
    with open('tokenised.train.txt', 'r') as file:
        lines = file.read()
        print(lines)
except FileNotFoundError:
    print("No file found")

dictTokens = ""

for line in lines:
        tokens = line.split()
        for token in tokens:
              if token not in dictTokens:
                   dictTokens = dictTokens + token + "\n"

try:
    with open('dictionary.txt', 'w') as file:
        file.write(dictTokens)
except FileNotFoundError:
    print("No file found")
"""
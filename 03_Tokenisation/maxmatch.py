import sys

sentences = sys.stdin.readlines()
dict = []

try:
    with open (sys.argv[1], 'r') as file:
        for line in file:
            dict.append(line[:len(line)-1])
except FileNotFoundError:
    print("No file found") 

def maxmatch(sentence, dict, app):
    if sentence == "":
        return app
    for i in range(len(sentence), 0, -1):
        firstword = sentence[:i]
        remainder = sentence[i:]
        if firstword in dict:
            app.append(firstword)
            return maxmatch(remainder, dict, app)
    firstword = sentence[:1]
    remainder = sentence[1:]
    app.append(firstword)
    return maxmatch(remainder, dict, app)
        
for sentence in sentences:
    print(*(maxmatch(sentence, dict, [])), end = '')



 
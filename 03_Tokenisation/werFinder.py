import sys

res = sys.stdin.readlines()

for line in res:
    if line[:4] == "WER:":
        print(line[5:len(line) - 2])
              
              
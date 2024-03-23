import sys

line = sys.stdin.readline()

while line:
    for token in line.strip().split(' '):
        if not token:
            continue
        if token[-1] in '!?':
            sys.stdout.write(token + '\n')
        elif token[-1] == '.':
            if token in ['O.M.', 'A.Y.', 'A.B.', 'N.B.', 'E.L.', 'P.E.N.', 'vs.', 'www.waste.', 'ycnm.edu.', 'te.noun.', 'M.A.', 'M.Sc.', 'm.', 'ysu.edu.', 'P.R.', 'F.C.', 'S.T.', 'e.g.', 'C.W.', 'W.L.', 'C.M.', 'M.A.', 'D.C.', 'P.E.']:
                sys.stdout.write(token + ' ')
            else:
                sys.stdout.write(token + '\n')
        else:
            sys.stdout.write(token + ' ')
    line = sys.stdin.readline()
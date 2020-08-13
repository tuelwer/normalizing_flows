import re
import sys

filename = sys.argv[1]

f = open(filename, 'r')
print('Open file:', filename)
nlls = []
for line in f:
    nll = re.findall(r"logp\(x\) = (.*) \+", line)
    if len(nll) > 0:
        nlls.append(float(nll[0]))

print('Minimum NLL:', min(nlls))

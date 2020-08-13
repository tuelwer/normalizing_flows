import re
import sys

filename = sys.argv[1]

f = open(filename, 'r')
print('Open file:', filename)
nlls = []
stds = []
for line in f:
    nll = re.findall(r"logp\(x\) = (.*) \+", line)
    std = re.findall(r"\+\/\- (.*)", line)
    print(std)
    if len(nll) > 0:
        nlls.append(float(nll[0]))
        stds.append(float(std[0]))

print('Maximal Log-Likelihood:', max(nlls))
print('Standard deviation:', stds[nlls.index(max(nlls))])

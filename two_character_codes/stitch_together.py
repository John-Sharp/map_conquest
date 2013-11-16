
lines1 = open("codes").readlines()
print lines1
lines2 = open("names").readlines()
print lines2

for z in zip(lines1, lines2):
    print z[0][:-1] + " " + z[1][:-1]

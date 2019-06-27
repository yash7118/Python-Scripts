f = open("demo19.py","r")

for line in f:
    print(line.strip("\n""\r"))
f.close()
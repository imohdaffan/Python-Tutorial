
with open("log.txt") as f:
    line = f.readlines()


lineno = 1
for line in line:
    if("python" in line):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1

else:
    print("No python is not present")
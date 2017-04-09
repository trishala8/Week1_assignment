lines = []

while True:
    s = raw_input(">> ")

    if not s:
        break;
    else:
        lines.append(s.upper())


for sentence in lines:
    print sentence

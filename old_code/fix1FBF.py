import fileinput

with fileinput.input() as f:
    for line in f:
        print(line.strip().replace("\u1FBF", "\u2019"))

import regex as re

file = open("rosalind_subs(2).txt", "r")
bigString = file.readline()
temp = file.readline()
compare = temp[:len(temp)-1:]

positions = [m.start() for m in re.finditer(compare, bigString, overlapped=1)]

print(bigString)
print("Substring to find:", end=" "),
print(compare)

print(positions)

for entry in positions:
    value = entry + 1
    print(value, end=' '),

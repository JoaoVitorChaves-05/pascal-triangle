def createLine(lines):
    last_line = lines[len(lines) - 1]
    new_line = list()

    for c in range(len(last_line) + 1):
        new_line.append(0)
    new_line[0] = 1
    new_line[len(new_line) - 1] = 1

    for position in range(len(new_line)):
        if new_line[position] == 0:
            try:
                soma = last_line[position] + last_line[position - 1]
                new_line[position] = soma
            except:
                pass
    return new_line

lines = [[1]]

n_lines = int(input("Number of lines to show: "))

for c in range(n_lines - 1):
    lines.append(createLine(lines))

for line in lines:
    print(line)
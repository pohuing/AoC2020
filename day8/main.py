with open("input") as f:
    programm = f.read().strip()

instructions = [[*line.split(), False] for line in programm.splitlines()]
counter = 0
acc = 0

while True:
    if instructions[counter][2]:
        print(acc)
        break

    instructions[counter][2] = True
    if instructions[counter][0] == "jmp":
        counter += int(instructions[counter][1])
    elif instructions[counter][0] == "nop":
        counter += 1
    elif instructions[counter][0] == "acc":
        acc += int(instructions[counter][1])
        counter += 1

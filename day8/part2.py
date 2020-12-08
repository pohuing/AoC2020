import copy

with open("input") as f:
    programm = f.read().strip()
#
# programm ="""nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

def brute_force(instructions):
    for i, inst in filter(lambda x: x[1][2] and x[1][0] == "nop" or x[1][0] == "jmp", enumerate(instructions)):
        working_instructions = copy.deepcopy(instructions)
        # Resetting visited status
        for line in working_instructions:
            line[2] = False

        if working_instructions[i][0] == "nop":
            working_instructions[i][0] = "jmp"
        else:
            working_instructions[i][0] = "nop"

        if res := run_computer(working_instructions):
            return res

def run_computer(instructions):
    """
    Mutates instructions to the result of a full run
    """
    counter = 0
    acc = 0

    while counter < len(instructions):
        if instructions[counter][2]:
            #print(acc)
            #print(f"Found loop start {counter}")
            return False

        old = counter
        instructions[counter][2] = True
        if instructions[counter][0] == "jmp":
            counter += int(instructions[counter][1])
        elif instructions[counter][0] == "nop":
            counter += 1
        elif instructions[counter][0] == "acc":
            acc += int(instructions[counter][1])
            counter += 1

    return acc



instructions = [[*line.split(), False] for line in programm.splitlines()]
run_computer(instructions)
print(brute_force(instructions))


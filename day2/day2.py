def part1():
    counter = 0
    with open("input") as f:
        for number, line in enumerate(f):
            print(f"Line {number}: {line}")
            bounds, letter, password = line.split(" ")
            lower, upper = bounds.split("-")
            letter = letter[0]
            password = password.strip("\n ")
            if password.count(letter) in range(int(lower), int(upper)+1):
                counter += 1
                print(f"Password {password} is valid")
            else:
                print(f"Password {password} is invalid")
    print(f"Total: {counter}")

def part2():
    counter = 0
    with open("input") as f:
        for number, line in enumerate(f):
            print(f"Line {number}: {line}")
            bounds, letter, password = line.split(" ")
            positions = bounds.split("-")
            letter = letter[0]
            password = password.strip("\n ")
            if 1 == [password[int(position)-1] == letter for position in positions].count(True):
                counter += 1
                print(f"Password {password} is valid")
            else:
                print(f"Password {password} is invalid")
    print(f"Total: {counter}")

if __name__ == "__main__":
    part2()
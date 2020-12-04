REQUIREMENTS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valids = 0

with open("input") as f:
    passports = f.read().split("\n\n")

for passport in passports:
    sections = {}
    passport = passport.replace("\n", " ")
    pairs = passport.strip().split(" ")
    for pair in pairs:
        key, value = pair.split(":")
        value: str = value.strip()
        #extra rules
        if key == "byr":
            if len(value) != 4:
                print(f"Found wrong year length {pair}")
                continue
            year = int(value)
            if 1920 <= year <= 2002:
                sections[key] = value
        elif key == "iyr":
            if len(value) != 4:
                print(f"Found wrong year length {pair}")
                continue
            year = int(value)
            if 2010 <= year <= 2020:
                sections[key] = value
        elif key == "eyr":
            if len(value) != 4:
                print(f"Found wrong year length {pair}")
                continue
            year = int(value)
            if 2020 <= year <= 2030:
                sections[key] = value
        elif key == "hgt":
            if "cm" in value:
                hgt = int(value.replace("cm", ""))
                if 150 <= hgt <= 193:
                    sections[key] = value
            elif "in" in value:
                hgt = int(value.replace("in", ""))
                if 59 <= hgt <= 76:
                    sections[key] = value
        elif key == "hcl":
            if len(value) == 7 and "#" == value[0] and all(char in "0123456789abcdef" for char in value[1:]):
                sections[key] = value
        elif key == "ecl":
            if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                sections[key] = value
        elif key == "pid":
            if value.isnumeric() and len(value) == 9:
                sections[key] = value
        elif key == "cid":
            pass
        else:
            print(f"Not recognized token {key} in {passport}")
    if all((requirement in sections for requirement in REQUIREMENTS)):
        print(f"Valid passport {sections}")
        valids += 1
    else:
        print(f"Invalid passport {sections} missing \n\t {set(REQUIREMENTS) - set(sections.keys())}")

print(valids)

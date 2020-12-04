requirements = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]#,"cid"]
valids = 0

passports = ""
with open("input") as f:
    passports = f.read()
#     passports = """eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007"""
    passports = passports.split("\n\n")




for passport in passports:
    sections = {}
    passport = passport.replace("\n", " ")
    pairs = passport.strip().split(" ")
    for pair in pairs:
        key, value = pair.split(":")
        value:str = value.strip()
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
    if all((requirement in sections for requirement in requirements)):
        print(f"Valid passport {sections}")
        valids+=1
    else:
        print(f"Invalid passport {sections} missing \n\t {set(requirements) - set(sections.keys())}")

print(valids)
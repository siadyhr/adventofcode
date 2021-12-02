def checkfields(passport):
    goods = []
    goods.append(1920 <= int(passport["byr"]) <= 2002)
    goods.append(2010 <= int(passport["iyr"]) <= 2020)
    goods.append(2020 <= int(passport["eyr"]) <= 2030)
    if passport["hgt"][-2:] == "cm":
        goods.append(150 <= int(passport["hgt"][:-2]) <= 193)
    elif passport["hgt"][-2:] == "in":
        goods.append(59 <= int(passport["hgt"][:-2]) <= 76)
    else:
        goods.append(False)
    goods.append(passport["hcl"][0] == "#" and len(passport["hcl"]) == 7 and
            len([x for x in passport["hcl"][1:] if x in "0123456789abcdef"]) == 6
            )
    goods.append(passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    goods.append(len(passport["pid"]) == 9 and len([x for x in passport["pid"] if x in "0123456789"]) == 9)
    print(goods)

    return all(goods)

def checkpassport(passport):
    passport = dict([field.split(":") for field in passport.split()])
    print(passport)
    if len([
        passport.get(field) for field in
            ["byr", "iyr", "eyr", "hgt", "hcl","ecl", "pid"]
            if field in passport
        ]) == 7:
        if checkfields(passport):
            print("OK")
            return 1
    print("Bad")
    return 0
    
goodpassports = 0
passport = ""
while True:
    rawin = input()
    if rawin == "EOF":
        break
    elif rawin:
        passport = passport + " " + rawin
    else:
        goodpassports += checkpassport(passport)
        passport = ""

print(goodpassports)

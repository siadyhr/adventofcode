def checkpassport(passport):
    passport = dict([field.split(":") for field in passport.split()])
    print(passport)
    if len([
        passport.get(field) for field in
            ["byr", "iyr", "eyr", "hgt", "hcl","ecl", "pid"]
            if field in passport
        ]) == 7:
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

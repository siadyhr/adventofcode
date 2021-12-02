good_passwords = 0
while True:
    rawin = input()
    if not rawin:
        print(good_passwords)
        quit()
    policy, password = rawin.split(":")
    ns, letter = policy.split(" ")
    nmin, nmax = [int(x) for x in ns.split("-")]
    password = password[1:]
#    print(nmin, nmax, letter, password)
    if nmin <= password.count(letter) <= nmax:
#        print(password.count(letter))
        good_passwords += 1


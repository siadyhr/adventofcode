good_passwords = 0
while True:
    rawin = input()
    if not rawin:
        print(good_passwords)
        quit()
    policy, password = rawin.split(":")
    ns, letter = policy.split(" ")
    n1, n2 = [int(x) for x in ns.split("-")]
    password = password[1:]
#    print(nmin, nmax, letter, password)
    if (password[n1-1] == letter) != (password[n2-1] == letter):
#        print(password.count(letter))
        good_passwords += 1


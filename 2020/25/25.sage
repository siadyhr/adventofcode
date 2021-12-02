pubkeys = []

R = Integers(20201227)
pubkeys.append(R(input()))
pubkeys.append(R(input()))
print(pubkeys)

secrets = [discrete_log(pubkey, R(7)) for pubkey in pubkeys]
private_keys = [pubkey ** secret for pubkey, secret in zip(pubkeys, secrets[::-1])]
print(secrets)
print(private_keys)

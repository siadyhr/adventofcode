from math import prod
hex_input = input()
bin_input = "".join("{:0>4}".format(bin(int(x, 16))[2:]) for x in hex_input )
print(len(bin_input))
print((bin_input[:20]))
bin_input = ((4 - len(bin_input)%4) % 4) * "0" + bin_input
print(len(bin_input))
print((bin_input[:20]))

def translate(transmission, amount=float('infinity'), length=None, depth=0):
#    print(">"*depth + "Will translate %s, max %s/%s" % (transmission, amount, length))
    if length is None:
        length = len(transmission) - 5
    translated = []
    i = 0
    while (i < length) and len(translated) < amount:
#        print(">"*depth + "Remaining: %s" % transmission[i:])
        if len(transmission) - i < 11:
            print(">"*depth +"Overlength")
            break
        version = int(transmission[i:i+3], 2)
        i += 3
        packet_type = int(transmission[i:i+3], 2)
        i += 3
        print(">"*depth + "v%s, type %s" % (version, packet_type))
        if packet_type == 4:
            data = ""
            while transmission[i] != "0":
                data += transmission[i+1:i+5]
                i += 5
            data += transmission[i+1:i+5]
            i += 5
            translated.append((version, packet_type, int(data, 2)))
        else:
            if transmission[i] == "0":
                # length type ID = 0
                i += 1
                sublength = int(transmission[i:i+15], 2)
                print(">"*depth + "Sublength", sublength)
                i += 15
                sub_translate, j = translate(transmission[i:i+sublength], length=sublength, depth = depth+1)
                translated.append((version, packet_type, sub_translate))
                i += sublength
            else:
                # length type ID = 1
                i += 1
                sub_amount = int(transmission[i:i+11], 2)
                i += 11
                print(">"*depth + "n_sub", sub_amount)
                sub_translate, j = translate(transmission[i:], amount = sub_amount, depth=depth+1)
                i += j
                translated.append((version, packet_type, sub_translate))

    return translated, i

def get_version_sum(data):
    result = 0
    for packet in data:
        result += packet[0]
        if type(packet[2]) is not int:
            result += get_version_sum(packet[2])

    return result

def parse(packet, depth=0):
    print(">"*depth, packet[1])
    if type(packet[2]) is int:
        return packet[2]

    print(len(packet[2]))

    def gt(gen):
        a, b = gen
        return 1 if a > b else 0
    def lt(gen):
        a, b = gen
        return 1 if a < b else 0
    def eq(gen):
        a, b = gen
        return 1 if a == b else 0
    def get(gen):
        for x in gen:
            return x

    function = {
        0 : sum,
        1 : prod,
        2 : min,
        3 : max,
        4 : get,
        5 : gt,
        6 : lt,
        7 : eq
    }

    operator_type = packet[1]
    return function[operator_type](parse(sub_packet, depth+1) for sub_packet in packet[2])

translation = translate(bin_input)[0]
print("Sum:")
print(get_version_sum(translation))
print(translation)
print("Parse:")
print(parse(translation[0]))

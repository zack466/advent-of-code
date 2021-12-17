with open("day16.in", 'r') as f:
    hex_input = f.readline().strip()

def int_to_bits(n):
    bits = []
    while n > 0:
        bits.append(n % 2)
        n //= 2
    return list(reversed(bits))

def left_pad(bits):
    if len(bits) < 4:
        return [0 for _ in range(4 - len(bits))] + bits
    return bits

def bits_to_int(bits):
    total = 0
    for i, b in enumerate(bits[::-1]):
        total += b << i
    return total

bits = []
for l in hex_input:
    bits.extend(left_pad(int_to_bits(int(l, 16))))

def take(n, bits):
    assert len(bits) >= n
    return bits[:n], bits[n:]

def parse_literal(bits):
    # print(bits)
    rest = bits
    num_bits = []
    while True:
        group, rest = take(5, rest)
        num_bits.extend(group[1:])
        if group[0] == 0:
            break
    return ("LITERAL", bits_to_int(num_bits)), rest

def parse_version(bits):
    group, rest = take(3, bits)
    return ("VERSION", bits_to_int(group)), rest

def parse_operator(bits, op_id):
    # print("parsing operator", bits)
    bit, rest = take(1, bits)
    # print("operator switch: ", bit[0])
    if bit[0] == 0:
        num_bits, rest = take(15, rest)
        length = bits_to_int(num_bits) # num bits in subpackets
        # print("subpacket bits", length)
        bits, rest = rest[:length], rest[length:]
        subpackets = []
        while len(bits) > 0:
            packet, bits = parse_packet(bits)
            subpackets.append(packet)
        return ("OPERATOR", op_id, subpackets), rest
    else:
        num_bits, rest = take(11, rest)
        length = bits_to_int(num_bits) # num subpackets
        # print("num subpackets", length)
        subpackets = []
        for _ in range(length):
            packet, rest = parse_packet(rest)
            subpackets.append(packet)
        return ("OPERATOR", op_id, subpackets), rest

def parse_packet(bits):
    version, rest = parse_version(bits)
    # print("parsing packet version: ", version)
    # dispatch on packet type
    type_bits, rest = take(3, rest)
    type = bits_to_int(type_bits)
    if type == 4: # literal
        literal, rest = parse_literal(rest)
        return (version, literal), rest
    else: # operator
        operator, rest = parse_operator(rest, type)
        return (version, operator), rest

def count_versions(packet):
    total = 0
    version, obj = packet
    total += version[1]
    type = obj[0]
    if type == "LITERAL":
        return total
    elif type == "OPERATOR":
        return total + sum(map(count_versions, obj[2]))

def solA():
    p, _ = parse_packet(bits)
    print(count_versions(p))

def prod(nums):
    iter = 1
    for n in nums:
        iter *= n
    return iter

def evaluate(packet):
    version, obj = packet
    type = obj[0]
    if type == "LITERAL":
        return obj[1]
    elif type == "OPERATOR":
        op_id = obj[1]
        if op_id == 0:
            return sum(map(evaluate, obj[2]))
        elif op_id == 1:
            return prod(map(evaluate, obj[2]))
        elif op_id == 2:
            return min(map(evaluate, obj[2]))
        elif op_id == 3:
            return max(map(evaluate, obj[2]))
        elif op_id == 5:
            return 1 if evaluate(obj[2][0]) > evaluate(obj[2][1]) else 0
        elif op_id == 6:
            return 1 if evaluate(obj[2][0]) < evaluate(obj[2][1]) else 0
        elif op_id == 7:
            return 1 if evaluate(obj[2][0]) == evaluate(obj[2][1]) else 0
        else:
            assert False

def solB():
    p, _ = parse_packet(bits)
    print(evaluate(p))

solB()

## Part A: ad-hoc stack parser thingy
# def sol(line: str):
#     toks = line.replace('(', ' ( ').replace(')', ' ) ').split()
#     i = 0
#     numstack = []
#     opstack = []
#     while i < len(toks):
#         # print(numstack, opstack)
#         if toks[i].isnumeric():
#             if len(opstack) and opstack[-1] == "+":
#                 numstack[-1] += int(toks[i]);
#                 opstack.pop()
#                 i += 1
#             elif len(opstack) and opstack[-1] == "*":
#                 numstack[-1] *= int(toks[i]);
#                 opstack.pop()
#                 i += 1
#             else:
#                 numstack.append(int(toks[i]))
#                 i += 1
#         elif toks[i] == "(":
#             opstack.append("(")
#             i += 1
#         elif toks[i] == ")":
#             assert opstack[-1] == "("
#             opstack.pop()
#             if len(opstack) and opstack[-1] == "+":
#                 num = numstack.pop()
#                 numstack[-1] += num;
#                 opstack.pop()
#             elif len(opstack) and opstack[-1] == "*":
#                 num = numstack.pop()
#                 numstack[-1] *= num;
#                 opstack.pop()
#             i += 1
#         elif toks[i] == "+":
#             opstack.append("+")
#             i += 1
#         elif toks[i] == "*":
#             opstack.append("*")
#             i += 1
#     return numstack[0]

# print(sol("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))


## Part B: a tiny recursive descent parser

# prod ::= sum (* sum)*
# sum ::= expr (+ expr)*
# expr ::= NUM | ( prod )

def parse_prod(toks):
    val, toks = parse_sum(toks)
    while len(toks) and toks[0] == "*":
        new_val, new_toks = parse_sum(toks[1:])
        val *= new_val
        toks = new_toks
    return val, toks

def parse_sum(toks):
    val, toks = parse_expr(toks)
    while len(toks) and toks[0] == "+":
        new_val, new_toks = parse_expr(toks[1:])
        val += new_val
        toks = new_toks
    return val, toks

def parse_expr(toks):
    if len(toks) and toks[0].isnumeric():
        return int(toks[0]), toks[1:]
    elif len(toks) and toks[0] == "(":
        val, toks = parse_prod(toks[1:])
        assert toks[0] == ")", "expected left paren"
        return val, toks[1:]
    else:
        assert False, "invalid expr"

def sol(line):
    toks = line.replace('(', ' ( ').replace(')', ' ) ').split()
    return parse_prod(toks)[0]

# print(sol("2 * 3 + (4 * 5)"))

with open("input_day18") as f:
    print(sum(map(sol, f.readlines())))

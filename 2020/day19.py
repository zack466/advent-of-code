from typing import Tuple

rules = {}

class Rule:
    def matches(self) -> bool:
        raise NotImplementedError()

class Char(Rule):
    def __init__(self, c: str):
        self.c = c;

    def matches(self, s: str):
        return (len(s) > 0 and s[0] == self.c), s[1:]

    def __repr__(self):
        return  f"\"{self.c}\""

class And(Rule):
    def __init__(self, rules):
        self.rules = rules

    def matches(self, s: str):
        remaining = s
        for rule in self.rules:
            parsed, rest = rule.matches(remaining)
            if parsed:
                remaining = rest
            else:
                return False, s
        return True, remaining

    def __repr__(self):
        return "And[" + " ".join(map(str, self.rules)) + "]"

class Or(Rule):
    def __init__(self, rules):
        self.rules = rules

    def matches(self, s: str):
        for rule in self.rules:
            parsed, rest = rule.matches(s)
            if parsed:
                return True, rest
        return False, s

    def __repr__(self):
        return "Or[" + " ".join(map(str, self.rules)) + "]"

class Pointer(Rule):
    def __init__(self, id):
        self.id = id

    def matches(self, s: str):
        return rules[self.id].matches(s)

    def __repr__(self):
        return f"{self.id}"

# rule ::= ID ":" (CHAR | or)
# or ::= and ("|" and)*
# and ::= ID+

def parse_and(toks):
    # print("and", toks)
    nums = []
    if len(toks) == 0 or not toks[0].isnumeric():
        return None, toks
    while len(toks) > 0 and toks[0].isnumeric():
        nums.append(Pointer(int(toks[0])))
        toks = toks[1:]
    return And(nums), toks

def parse_or(toks):
    # print("or", toks)
    rules = []
    rule, toks = parse_and(toks)
    if not rule:
        return None, toks
    rules.append(rule)
    while len(toks) > 0 and toks[0] == "|":
        rule, toks = parse_and(toks[1:])
        if not rule:
            assert False, "should parse"
        rules.append(rule)
    return Or(rules), toks

def parse_rule(s: str) -> Tuple[int, Rule]:
    toks = s.split()
    id: int = int(toks[0][:-1])
    if toks[1][0] == "\"":
        return id, Char(toks[1][1])
    rule, toks = parse_or(toks[1:])
    if rule:
        assert len(toks) == 0
        return id, rule
    else:
        assert False, "bad rule parse"

# part A
def sol(input: str) -> int:
    rules_str, cases_str = input.split("\n\n")
    for line in rules_str.split("\n"):
        id, rule = parse_rule(line)
        rules[id] = rule

    counter = 0
    for line in cases_str.split("\n"):
        if len(line) == 0:
            continue
        parsed, res = rules[0].matches(line)
        if parsed and len(res) == 0:
            counter += 1
    return counter

# part B
# 8: 42+
# 11: 42+n 31+n

with open("input_day19") as f:
    print(sol(f.read()))

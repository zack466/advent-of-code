const input = Deno.readTextFileSync("day8.in");
const lines = input.trim().split("\n");

const ALPHA = ["a", "b", "c", "d", "e", "f", "g"];
const DECODE: any = {
  "abcefg": "0",
  "cf": "1",
  "acdeg": "2",
  "acdfg": "3",
  "bcdf": "4",
  "abdfg": "5",
  "abdefg": "6",
  "acf": "7",
  "abcdefg": "8",
  "abcdfg": "9",
};

const ENCODE: any = {
  "0": "abcefg",
  "1": "cf",
  "2": "acdeg",
  "3": "acdfg",
  "4": "bcdf",
  "5": "abdfg",
  "6": "abdefg",
  "7": "acf",
  "8": "abcdefg",
  "9": "abcdfg",
};

const compareLetter = (a: string, b: string) => {
  if (a === b) {
    return 0;
  } else if (a < b) {
    return -1;
  } else {
    return 1;
  }
};

function getDigit(x: string) {
  let letters = x.split("");
  letters.sort(compareLetter);
  return DECODE[letters.join("")];
}

const hasLength = (n: number) => (x: string) => x.length === n;
const cleanSplit = (delim: string) => (x: string) => x.trim().split(delim);

function solA() {
  let count = 0;
  for (let line of lines) {
    let [patterns, output] = line.split("|").map(cleanSplit(" "));
    for (let out of output) {
      if ([2, 3, 4, 7].find((x: number) => x === out.length)) {
        count += 1;
      }
    }
  }
  console.log(count);
}

function reduce(rules: any) {
  for (let key1 in rules) {
    for (let key2 in rules) {
      if (key1 === key2) continue;
      if (contains(key1, key2)) {
        let new_rule = difference(key1, key2);
        let new_vals = difference(rules[key1], rules[key2]);
      }
    }
  }
}

function solB() {
  for (let line of lines) {
    let rules: any = {}; // Set(encoded) <=> Set(decoded)
    let [patterns, output] = line.split("|").map(cleanSplit(" "));
    patterns.find(hasLength(2));
    for (let pattern of patterns) {
    }
  }
}

solA();

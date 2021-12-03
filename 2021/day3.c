#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define INFILE "day3.in"
#define MAX_LINES 1005

#define is_bit(mask, pos) (mask & (1 << pos)) != 0
#define clear(arr) memset(arr, 0, sizeof arr)

int LINES = 0;
int BITS = 0;
int lines[MAX_LINES];

// record nums into an array
int init() {
    const char mode = 'r';
    FILE *f = fopen(INFILE, &mode);
    // check how many bits per line
    while (1) {
        char c;
        fscanf(f, "%c", &c);
        if (c == '\n') break;
        BITS++;
    }
    rewind(f);

    // read all values into lines
    while (!feof(f)) {
        int val = 0;
        for (int i = 0; i < BITS; i++) {
            char c;
            fscanf(f, "%c", &c);
            if (c == '1') {
                val += 1 << BITS - 1 - i;
            }
        }
        fscanf(f, "\n"); // eat newline
        lines[LINES] = val;
        LINES++;
    }
    fclose(f);
}

void solA() {
    int common_bits[BITS];
    clear(common_bits);
    for (int i = 0; i < BITS; i++) {
        int count = 0;
        for (int line = 0; line < LINES; line++) {
            if (is_bit(lines[line], i)) {
                count++;
            }
        }
        if (count > LINES / 2) {
            common_bits[i] = 1;
        }
    }
    int gamma = 0, epsilon = 0;
    for (int i = 0; i < BITS; i++) {
        gamma += common_bits[i] << i;
        epsilon += !common_bits[i] << i;
    }
    printf("%d %d\n", gamma, epsilon);
    printf("%d\n", gamma * epsilon);
}

int numRemaining(int filtered[]) {
    int count = 0;
    for (int i = 0; i < LINES; i++) {
        if (!filtered[i]) count++;
    }
    return count;
}

int countRemainingWithBit(int filtered[], int n, int bit) {
    int count = 0;
    for (int i = 0; i < LINES; i++) {
        if (!filtered[i]) {
            if ((lines[i] & (1 << n)) == (bit << n)) {
                count++;
            }
        }
    }
    return count;
}

void filterLines(int filtered[], int n, int bit) {
    // printf("Filter at %d with %d\n", n, bit);
    for (int i = 0; i < LINES; i++) {
        if (!filtered[i]) {
            if (is_bit(lines[i], n) && bit == 1) {
                filtered[i] = 1;
            } else if ((!is_bit(lines[i], n)) && bit == 0) {
                filtered[i] = 1;
            }
        }
    }
}

int getLine(int filtered[]) {
    for (int i = 0; i < LINES; i++) {
        if (!filtered[i]) return lines[i];
    }
}

void printBinary(int num) {
    for (int i = BITS-1; i >= 0; i--) {
        printf("%d", (num & (1 << i)) != 0);
    }
}

void printLines(int filtered[]) {
    for (int i = 0; i < LINES; i++) {
        printBinary(lines[i]);
        printf("\t%d\n", filtered[i]);
    }
}

void solB() {
    int filtered[MAX_LINES];
    clear(filtered);
    for (int n = BITS - 1; n >= 0; n--) {
        // printLines(filtered);
        int remaining = numRemaining(filtered);
        if (remaining == 1) break;
        int numOnes = countRemainingWithBit(filtered, n, 1);
        if (numOnes * 2 >= remaining) {
            filterLines(filtered, n, 0);
        } else {
            filterLines(filtered, n, 1);
        }
    }
    int o2 = getLine(filtered);
    clear(filtered);
    for (int n = BITS - 1; n >= 0; n--) {
        // printLines(filtered);
        int remaining = numRemaining(filtered);
        if (remaining == 1) break;
        int numZeros = countRemainingWithBit(filtered, n, 0);
        if (numZeros * 2 > remaining) {
            filterLines(filtered, n, 0);
        } else {
            filterLines(filtered, n, 1);
        }
    }
    int co2 = getLine(filtered);
    printf("%d %d\n", o2, co2);
    printf("%d\n", o2 * co2);
}

int main() {
    init();
    solB();
    return 0;
}

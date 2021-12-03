#include <stdio.h>
#include <stdlib.h>

#define BITS 12

int bits_count[BITS];

int solA() {
    const char mode = 'r';
    FILE *f = fopen("day3.in", &mode);
    int line_count = 0;
    while (!feof(f)) {
        line_count++;
        for (int i = 0; i < BITS; i++) {
            char c;
            fscanf(f, "%c", &c);
            if (c == '1') {
                bits_count[i]++;
            }
        }
        fscanf(f, "\n"); // eat newline
    }

    int gamma = 0, epsilon = 0;
    for (int i = 0; i < BITS; i++) {
        int exp = BITS - 1 - i; // 2^exp, going from MSB to LSB
        if (bits_count[i] > line_count / 2) {
            // gamma bit 1
            gamma += 1 << exp;
        } else {
            epsilon += 1 << exp;
        }
    }
    printf("%d\n", gamma * epsilon);
    fclose(f);
}

int main() {
    solA();
    return 0;
}

#include <bits/stdc++.h>

using namespace std;


int main() {
	freopen("day2_input", "r", stdin);
	int cc = 0;
	for (int i=0; i<1001; i++) {
		int low, high;
		char c;
		char str[1024];
		memset(str, '\0', 1024);
		scanf("%d-%d %c: %s\n", &low, &high, &c, str);
		int count = 0;
		/* part 1
		for (char x : str)
			if (x == c) ++count;
		if (count >= low && count <= high) ++cc;
		*/
		if (str[low-1] == c ^ str[high-1] == c) ++cc;
	}
	printf("%d\n", cc);
	return 0;
}

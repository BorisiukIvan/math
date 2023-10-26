#include <stdio.h>
int main() {
    long long x = 1000000;
    char arr[x];
    arr[0] = '0';
    arr[1] = '0';
    for (long long i = 2; i < x; i++) arr[i] = '1';
    long long s = 1;
    for (long long i = 0; i < x; i++) {
	if (arr[i] == '0') continue;
	printf("%llu\n", i);
	for (long long j = i*i; j < x; j = j + i) arr[j] = '0';
    };
};
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>

int write_to_file(char buffer[255]) {
    FILE *fp = fopen("CHERNOVIK2", "a");
    fputs(strcat(buffer, "\n"), fp);
    fclose(fp);
    return 0;
};

int ncd(unsigned long long x, unsigned long long y) {
    unsigned long long c;
    if (y > x) {
        c = x;
        x = y;
        y = c;
    };
    unsigned long long n = y;
    while (x%y) {
        c = x;
        x = y;
        y = c % y;
    };
    return y;
}


unsigned long long raiseTo(unsigned long long base, unsigned long long power){
    unsigned long long result = 1,i;
    for (i=0; i<power;i++) {
        result*=base;
    }
    return result;
}

unsigned long long properDivisorSum(unsigned long long n, long k, long z){
	unsigned long long prod = 1; 
	unsigned long long temp = n,i,count = 0;

//	if ((n % 3 == 0) || (n % 5 == 0) || ( (n < 477897252090) && (n % 23 == 0) )) return 1;
//	if ((ncd(n, 819) > 1) && (ncd(n, 135) > 1)) return 1;
//	if ( (n % 5 == 0) || (n % 2 == 0) || (n % 31 == 0) ) return 1;
	while(n%2 == 0){
		count++;
		n /= 2;
	}
	
	if(count!=0)
		prod *= (raiseTo(2,count + 1) - 1);

	for(i=3;i*i<=n;i+=2){
		count = 0;
		
		while(n%i == 0){
			count++;
			n /= i;
		}
		
		if(count==1)
			prod *= (i+1);
		else if(count > 1)
			prod *= ((pow(i,count + 1) - 1)/(i-1));
	}
	
	if(n>2)
		prod *= (n+1);

	if (prod % z) return 1;
	return (prod / z * k) - temp;
}

void printSeries(unsigned long long* arr,int size,long k,long z,char* type){
//	return;
//	if (strcmp(type, "Sociable")) return;
//	if ( size < 3 ) return;
//	if ( arr[size-1] == arr[size-3] ) return;
	int i;
	char buffer[256];

	sprintf(buffer, "\nInteger : %llu, Type : %s, Parameter1 : %llu, Parameter2 : %llu, Series : ",arr[0],type,k,z);
	write_to_file(buffer);
	printf("\nInteger : %llu, Type : %s, Parameter1 : %llu, Parameter2 : %llu, Series : ",arr[0],type,k,z);

	for(i=0;i<size-1;i++) {
		printf("%llu, ",arr[i]);
		sprintf(buffer, "%llu, ",arr[i]);
		write_to_file(buffer);
	};

	printf("%llu\n",arr[i]);
	sprintf(buffer, "%llu\n", arr[i]);
	write_to_file(buffer);
	fflush(stdout);
}

void aliquotClassifier(unsigned long long n, long k, long z){
	unsigned long long arr[8];
	int i,j;
	
	arr[0] = n;
	
	for(i=1;i<8;i++){
		arr[i] = properDivisorSum(arr[i-1], k, z);
		if(arr[i] < 2) return;
		if(ncd(arr[i], z) > 1) return;
		if(arr[i] > n) return;
		if(arr[i] == arr[i-1]) return;
		if (arr[i] == n) {
			if (i < 1) return;
			printSeries(arr,i+1,k,z,(arr[i]==n && i==2)?"Amicable":"Sociable");
			return;
		}
		
		for(j=1;j<i;j++) {
			if(arr[j]==arr[i]) return;
		}
	}
	
//	printSeries(arr, i+1, k, z, "Non-Terminating!");
}

/*int main()
{
	long x = 844000;
	long z, s, i, z_temp;
	while (1) {
// Для каждого х берем z как сумму его делителей
		z = properDivisorSum(x, 1, 1) + x;
		for (long i = z; i < 2*x; i++) {
//			printf("%llu %llu %llu %llu %llu\n", x, i/ncd(i, z), z/ncd(i, z), i, z);
//			if (i < 7/4*x) continue;
			z_temp = ncd(i, z);
			if (properDivisorSum(z/z_temp, 1, 1) + z/z_temp > i/z_temp) continue;
			aliquotClassifier(x, i/z_temp, z/z_temp);
		};
		x = x + 1;
		if (x % 1000 == 0) {
			printf("%llu\n", x);
			fflush(stdout);
		};
	};
};*/

/*int main()
{
// Просчитано до k = 673
	long k = 34;
	while (1) {
		for (long z = k/2; z < k; z++) {
			if ((k == 34) && (z < 25)) continue;
			if (z*2 <= k) continue;
//			printf("Okay. z = %llu; k = %llu", z, k);
			if (ncd(k, z) > 1) continue;
//			printf("Okay. z = %llu; k = %llu", z, k);
			if (properDivisorSum(z, 1, 1) > k - z) continue;
//			printf("Okay. z = %llu; k = %llu", z, k);
			for (long i = 2; i < 100000000; i++) {
//				if ((k == 7) && (z == 4)) printf("Okay. i = %llu; k = %llu; z = %llu;\n", i, k, z);
				if (ncd(i, z) > 1) continue;
				aliquotClassifier(i, k, z);
			};
//			printf("Okay. z = %llu; k = %llu", z, k);
			printf("k = %llu, z = %llu\n", k, z);
		};
		k = k + 1;
	};
}*/

int main()
{
	char buffer[39];
	int k, z;
	while (1) {
		scanf("%s", buffer);
		k = atoi(buffer);
		scanf("%s", buffer);
		z = atoi(buffer);
		for (long i = 2; i < 100000000; i++) {
			if (ncd(i, z) > 1) continue;
			aliquotClassifier(i, k, z);
		};
	}
}

/*int main() {
    long k = 96;
    long z = 73;
    long x = 1;
    while (1) {
	x = x + 2;
	if (x % 3 == 0) continue;
// || (x % 11 == 0) || (x % 13 == 0) || (x % 17 == 0) || (x % 19 == 0) || (x % 23 == 0) || (x % 29 == 0) || (x % 31 == 0) || (x % 37 == 0) || (x % 41 == 0) || (x % 43 == 0) || (x % 97 == 0)) continue;
	aliquotClassifier(x, k, z);
//	if (x % 10000000 == 1) printf("%llu\n", x);
    };
};*/


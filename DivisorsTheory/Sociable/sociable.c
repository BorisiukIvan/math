/*
    This programm was written on December 2024 by Ivan Borysiuk.
    If you have any feedback, you can contact me at borisiuk.ivan.224@gmail.com.
*/


#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<map>
#include<iostream>
#include<ostream>

std::map<long long, long long> m;
//long long a[100000000];

int write_to_file(char buffer[255]) {
    FILE *fp = fopen("SOCIABLE_T", "a");
    fputs(strcat(buffer, "\n"), fp);
    fclose(fp);
    return 0;
};

unsigned long long ncd(unsigned long long x, unsigned long long y) {
    if (y > x) return ncd(y, x);
    if (x % y == 0) return y;
    return ncd(y, x%y);
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
		prod *= (pow(2,count + 1) - 1);

	count = 0;
	while (n%3 == 0){
		count++;
		n /= 3;
	}
	if (count != 0) prod *= ((pow(3, count+1) - 1)/2);

	for(i=5;i*i<=n;i=i+2*(3-i%3)){
		count = 0;
		
		while(n%i == 0){
			count++;
			n /= i;
//			f = pow(n,0.5);
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

void printSeries(unsigned long long* arr,int size,long k,long z){
//	return;
//	if (strcmp(type, "Sociable")) return;
//	if ( size < 3 ) return;
//	if ( arr[size-1] == arr[size-3] ) return;
	int i;
	char buffer[256];

	sprintf(buffer, "\nInteger : %llu, Parameter1 : %llu, Parameter2 : %llu, Series : ",arr[0],k,z);
	write_to_file(buffer);
	printf("\nInteger : %llu, Parameter1 : %llu, Parameter2 : %llu, Series : ",arr[0],k,z);

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

void aliquotClassifier(unsigned long long n, long k, long z, unsigned long long v){
	unsigned long long arr[8];
	int i,j;
	
	arr[0] = v;
	
	for(i=1;i<8;i++){
//		s = a[arr[i-1]-1];
		arr[i] = properDivisorSum(arr[i-1], k, z);
//		arr[i] = s/z*k-arr[i-1];
//		std::cout << arr[i-1] << " " << s << " " << z << " " << k << " " << arr[i] << std::endl;
		if(arr[i] < 2) return;
		if(ncd(arr[i], z) > 1) return;
		if(arr[i] > n) return;
		if(arr[i] == arr[i-1]) return;
		if (arr[i] == n){
			if (i==1) return;
			printSeries(arr,i+1,k,z);
			return;
		}
		
		for(j=1;j<i;j++) {
			if(arr[j]==arr[i]) return;
		}
	}
	
//	printSeries(arr, i+1, k, z, "Non-Terminating!");
}

int main()
{
	long x = 3;
	long z, s, i, z_temp;
	long t0, t1;
	while (1) {
		z = properDivisorSum(x, 1, 1) + x;
//		a[x-1] = z;
		for (long i = z+1; i < 2*x; i+=1) {
			z_temp = ncd(i, z);
			t0 = z/z_temp;
			if (t0 > 10000) continue;
			if (m.count(t0)) {
				t1 = m[t0];
			} else {
				t1 = properDivisorSum(t0, 1, 1) + t0;
				m[t0] = t1;
			};
			if (t1 > i/z_temp) continue;
			aliquotClassifier(x, i/z_temp, t0, i-x);
		};
		x = x + 1;
		if (x % 1000 == 0) {
			printf("%llu\n", x);
			fflush(stdout);
		};
	};
};

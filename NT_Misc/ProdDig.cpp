#include <iostream>


int main() {
// If you want to customise starting value of x0, you need to change prod to product of digits of x0
// I checked all x0 below 11 111 111 111.
    long x0 = 1;
    long prod = 1;
    long ld, x, x2;

    while (1) {
	x = x0*prod;
	while ((x>9) && (x%10<2)) x /= 10;
	if (x == 1) std::cout<<x0<<" * "<<prod<<" = "<<x0*prod<<std::endl;
//	if (x0 == 72215) std::cout<<x0<<" * "<<prod<<" = "<<x0*prod<<std::endl;
	x2 = x0 + 1;
	ld = 1;
	while (x2 % 10 == 0) {
		prod /= 9;
		x2 /= 10;
		ld *= 10;
	}
	if (x2 % 10 > 1) {
		prod /= (x2%10 - 1);
		prod *= (x2%10);
	}
	x0 = x0 + 1 + (ld - 1)/9;
//	std::cout<<x0<<" "<<prod<<std::endl;
    }
    
    return 0;
}
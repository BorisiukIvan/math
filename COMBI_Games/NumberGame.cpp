#include <iostream>
#include <vector>

int check(int x, std::vector<int> path, int c) {
    int depth = 9;
    int mx = depth*depth;
    int y;

    for (auto i:path) {
	if (i == x) return 0;
    }
    if (x > mx) return 0;
    std::vector<int> path2 = path;
    path2.push_back(x);
    for (int i = 2; i <= depth; i++) {
        if (x*i <= mx) {
            y = check(x*i, path2, 0);
	    if (c == 1) std::cout<<x<<" "<<x*i<<" => "<<y<<std::endl;
            if (y == 1) return 0;
	}
        if (x % i == 0) {
           y = check(x/i, path2, 0);
	   if (c == 1) std::cout<<x<<" "<<x/i<<" => "<<y<<std::endl;
           if (y == 1) return 0;
	}
    }
    if (c == 1) std::cout<<x<<" => 1"<<std::endl;
    return 1;
}

int main() {
    int y = check(1, (std::vector<int>) {}, 1);
    std::cout<<y<<std::endl;
}
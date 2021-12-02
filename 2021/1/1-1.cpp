#include <iostream>
int main() {
	std::cout << "Hello, World!" << "\n";
	int increases = 0;
	int last, current;

	int loops = 0;
	std::cout << increases << "\n";
	while (std::cin >> current) {
		if (current > last) {
			increases += 1;
		}
		loops += 1;
		last = current;
	}

	std::cout << increases << "\n";
	std::cout << loops;

	return 1;
}

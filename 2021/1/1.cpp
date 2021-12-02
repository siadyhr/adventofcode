#include <iostream>
#include <numeric>

int main() {
	std::cout << "Hello, World!" << "\n";
	int increases = 0;
	int last, current;
	int last_sum;

	int index = 0;
	int window[3] = {0, 0, 0};
	int sum = 0;
	int loops = 0;
	std::cout << increases << "\n";

	for (int i = 0; i < 3; i++) {
		std::cin >> window[i];
	}
	while (std::cin >> current) {
		window[index] = current;
		index = (index + 1) % 3;

		if (std::accumulate(window, window+3, 0) > last_sum) {
			increases += 1;
		}
		last_sum = std::accumulate(window, window+3, 0);
		std::cout << "#" << last_sum << "\n";
	}

	std::cout << increases << "\n";

	return 1;
}

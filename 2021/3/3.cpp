#include <iostream>
#include <string>
#include <cmath>
#include <typeinfo>

const int N = 12;

int part1(std::string diagnostics[], int width, int length) {
	int ones[width];
	for (int i = 0; i < width; ++i) {
		ones[i] = 0;
	}

	for (int line = 0; line < length; ++line) {
		for (int pos = 0; pos < width; ++pos) {
			if (diagnostics[line][pos] == '1') {
				ones[pos] += 1;
			}
		}
	}
	int gamma = 0;
	int epsilon = 0;
	for (int i = 0; i < width; ++i) {
		if (ones[i] > N/2) {
			gamma += std::pow(2, width-i-1);
		} else {
			epsilon += std::pow(2, width-i-1);
		}
	}
	for (int i = 0; i < width; ++i) {
		std::cerr << ones[i] << " ";
	}
	std::cerr << "\n";
	return gamma * epsilon;
}

int main() {
	std::string line;
	std::cin >> line;
	int width = line.length();
	std::string diagnostics[N];

	diagnostics[0] = line;
	for (int i = 1; i < N; ++i) {
		std::cin >> diagnostics[i];
	}

	std::cout << part1(diagnostics, width, N) << "\n";

	return 1;
}

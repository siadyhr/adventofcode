#include <iostream>
#include <string>
#include <cmath>
#include <typeinfo>
#include <vector>

const int N = 1000;

std::vector<int> get_commons(std::vector<std::string> diagnostics, int width, int length) {
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
	std::vector<int> result;
	for (int i = 0; i < width; ++i) {
		if (ones[i] >= N/2) {
			result.push_back(1);
		} else {
			result.push_back(0);
		}
	}
	/*
	for (int i = 0; i < width; ++i) {
		std::cerr << ones[i] << " ";
	}
	std::cerr << "\n";
	*/
	return result;
}

int vec2int(std::vector<int> vector) {
	int result = 0;
	int i = 0;
	for (auto & x : vector) {
//		std::cerr << i << " " << x << "\n";
		result += x * std::pow(2, vector.size() - i - 1);
		++i;
	}
	return result;
}

std::vector<int> twos_complement(std::vector<int> vector) {
	std::vector<int> result;
	for (auto & x : vector) {
		if (x == 1) {
			result.push_back(0);
		} else {
			result.push_back(1);
		}
	}
	return result;
}

int part1(std::vector<int> most_common) {
	return vec2int(twos_complement(most_common)) * vec2int(most_common);
}

int main() {
	std::string line;
	std::cin >> line;
	int width = line.length();
	std::vector<std::string> diagnostics;

	diagnostics.push_back(line);
	while (std::cin >> line) {
		diagnostics.push_back(line);
	}

	std::vector<int> most_common = get_commons(diagnostics, width, N);

	// Part 1
	std::cout << part1(most_common);

	// Part 2
	std::cout << part2(diagnostics, most_common) << "\n";

	return 1;
}

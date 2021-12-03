#include <iostream>
#include <string>
#include <cmath>
#include <typeinfo>
#include <vector>

int N = 0;

std::vector<int> get_commons(std::vector<std::string> diagnostics, std::vector<bool> allowed_indices, int n_allowed_indices, bool reverse = false) {
	int width = diagnostics[0].size();
	int length = diagnostics.size();
	int ones[width];
	for (int i = 0; i < width; ++i) {
		ones[i] = 0;
	}

	for (int line = 0; line < length; ++line) {
		if (!allowed_indices[line]) {
			continue;
		}
		for (int pos = 0; pos < width; ++pos) {
			if (diagnostics[line][pos] == '1') {
				ones[pos] += 1;
			}
		}
	}
	std::vector<int> result;
	for (int i = 0; i < width; ++i) {
		if (reverse) {
			result.push_back(1 * (ones[i] < n_allowed_indices - n_allowed_indices/2));
		} else {
			result.push_back(1 * (ones[i] >= n_allowed_indices - n_allowed_indices/2));
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

int rating(std::vector<std::string> diagnostics, bool reverse = false) {
	for (int pos = 0; pos < diagnostics[0].size(); ++pos) {
	}
	std::vector<bool> allowed_indices(diagnostics.size(), true);
	int n_allowed = diagnostics.size();
	std::vector<int> most_common;

	int pos = 0;
	while (n_allowed > 1) {
//		std::cerr << "loop" << pos << "\n";
		most_common = get_commons(diagnostics, allowed_indices, n_allowed, reverse);
		for (int i = 0; i < diagnostics.size(); ++i) {
			if (allowed_indices[i] && (
						(int)diagnostics[i][pos]-48 != most_common[pos]
					)
			   ) {
//				std::cerr << n_allowed << "Forkast i = " << i << "," << diagnostics[i] << "\n";
				allowed_indices[i] = false;
				n_allowed -= 1;
			}
		}
		pos += 1;
	}
	for (int i = 0; i < diagnostics.size(); ++i) {
		if (allowed_indices[i]) {
//			std::cerr << diagnostics[i] << "!\n";
			return std::stoi(diagnostics[i], 0, 2);
		}
	}
	return -1;
	/*
	std::vector<int> ratings;
	int rating = 0;
	for (auto & diagnostic : diagnostics) {
		rating = 0;
		for (int i = 0; i < diagnostic.size(); ++i) {
			// 48 is ASCII(0) -- (int)0
			if ((int)diagnostic[i] - 48 == most_common[i]) {
				rating += 1;
			} else {
				break;
			}
		}
		ratings.push_back(rating);
	}
	return ratings;
	*/
}

int max_index(std::vector<int> input) {
	int max_i = 0;
	int i = 0;
	int max_value = input[0];
	for (auto & x : input) {
		if (x > max_value) {
			max_i = i;
			max_value = x;
		}
		++i;
	}
	return max_i;
}

int part1(std::vector<int> most_common) {
	return vec2int(twos_complement(most_common)) * vec2int(most_common);
}

int part2(std::vector<std::string> diagnostics) {
	int O2 = rating(diagnostics);
	int CO2 = rating(diagnostics, true);
	std::cout << O2 << "," << CO2 << "\n";
	return rating(diagnostics) * rating(diagnostics, true);
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
	N = diagnostics.size();

	std::vector<bool> allowed_indices(N, true);
	std::vector<int> most_common = get_commons(diagnostics, allowed_indices, N);

	// Part 1
	std::cout << "Part 1: " << part1(most_common) << "\n";

	// Part 2
	std::cout << part2(diagnostics) << "\n";

	return 1;
}

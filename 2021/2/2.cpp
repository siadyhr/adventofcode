#include <iostream>
#include <string>

const int N = 1000;

int part1(std::string instructions[], int magnitudes[]) {
	int position = 0;
	int depth = 0;

	for (int i = 0; i < N; ++i) {
		if (instructions[i] == "forward") {
			position += magnitudes[i];
		} else if (instructions[i] == "up") {
			depth -= magnitudes[i];
		} else {
			depth += magnitudes[i];
		}
	}
	return position * depth;
}

int part2(std::string instructions[], int magnitudes[]) {
	int aim = 0;
	int position = 0;
	int depth = 0;

	for (int i = 0; i < N; ++i) {
		if (instructions[i]== "forward") {
			position += magnitudes[i];
			depth += (magnitudes[i] * aim);
		} else if (instructions[i] == "up") {
			aim -= magnitudes[i];
		} else {
			aim += magnitudes[i];
		}
	}
	return position * depth;
}


int main() {
	std::string instructions[N];
	int magnitudes[N];

	for (int i = 0; i < 1000; ++i) {
		std::cin >> instructions[i];
		std::cin >> magnitudes[i];
	}
	std::cout << part1(instructions, magnitudes) << "\n";
	std::cout << part2(instructions, magnitudes) << "\n";

	return 1;
}

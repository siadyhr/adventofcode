#include <iostream>
#include <string>

int part1() {
	std::string direction;
	int magnitude;
	int position = 0;
	int depth = 0;

	while (std::cin >> direction >> magnitude) {
		if (direction == "forward") {
			position += magnitude;
		} else if (direction == "up") {
			depth -= magnitude;
		} else {
			depth += magnitude;
		}
	}
	return position * depth;
}

int part2() {
	std::string direction;
	int aim = 0;
	int magnitude;
	int position = 0;
	int depth = 0;

	while (std::cin >> direction >> magnitude) {
		if (direction == "forward") {
			position += magnitude;
			depth += (magnitude * aim);
		} else if (direction == "up") {
			aim -= magnitude;
		} else {
			aim += magnitude;
		}
	}
	return position * depth;
}


int main() {
//	std::cout << part1() << "\n";
	std::cout << part2() << "\n";

	return 1;
}

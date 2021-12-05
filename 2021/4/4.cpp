#include <iostream>
#include <string>
#include <cmath>
#include <typeinfo>
#include <vector>
#include <map>
#include <tuple>

std::tuple<int, int> get_winning_board(
	std::vector<int> numbers,
	std::map<int, std::vector<int>> num_to_board,
	std::map<int, std::map<int, std::tuple<int, int>>> num_location,
	int n_boards
	) {

	// cols/rows contains boards, each a vector with fill
	// level of corresponding col/row
	std::map<int, std::vector<int>> cols;
	std::map<int, std::vector<int>> rows;
	for (int j = 0; j < n_boards; ++j) {
		cols[j] = std::vector<int>(5, 0);
		rows[j] = std::vector<int>(5, 0);
	}
	int winning_board;
	int winning_number;
	for (auto & number : numbers) {
//		std::cerr << "Fik " << number << ", er i ";
		for (auto & board : num_to_board[number]) {
//			std::cerr << board << ", ";
//			std::cerr << "r" << std::get<0>(num_location[board][number]);
//			std::cerr << "c" << std::get<1>(num_location[board][number]) << "|";
			rows[board][std::get<0>(num_location[board][number])] += 1;
			cols[board][std::get<1>(num_location[board][number])] += 1;

			if (
				rows[board][std::get<0>(num_location[board][number])] == 5
				or
				cols[board][std::get<1>(num_location[board][number])] == 5
			   ) {
				winning_board = board;
				winning_number = number;
				goto game_won;
			}
		}
//		std::cerr << "\n";
	}
game_won:
//	std::cerr << "Board " << winning_board << " won" << "\n";
//	std::cerr << winning_number;
	return std::make_tuple(winning_board, winning_number);
}

std::tuple<int, int> get_last_board(
	std::vector<int> numbers,
	std::map<int, std::vector<int>> num_to_board,
	std::map<int, std::map<int, std::tuple<int, int>>> num_location,
	int n_boards
	) {

	// cols/rows contains boards, each a vector with fill
	// level of corresponding col/row
	std::map<int, std::vector<int>> cols;
	std::map<int, std::vector<int>> rows;
	for (int j = 0; j < n_boards; ++j) {
		cols[j] = std::vector<int>(5, 0);
		rows[j] = std::vector<int>(5, 0);
	}
	std::vector<bool> finished_boards(n_boards, false);
	int n_boards_left = n_boards;
	int last_board;
	int last_number;
	for (auto & number : numbers) {
//		std::cerr << "Fik " << number << ", er i ";
		for (auto & board : num_to_board[number]) {
			if (finished_boards[board]) {
				continue;
			}
			
//			std::cerr << board << ", ";
//			std::cerr << "r" << std::get<0>(num_location[board][number]);
//			std::cerr << "c" << std::get<1>(num_location[board][number]) << "|";
			rows[board][std::get<0>(num_location[board][number])] += 1;
			cols[board][std::get<1>(num_location[board][number])] += 1;

			if (
				rows[board][std::get<0>(num_location[board][number])] == 5
				or
				cols[board][std::get<1>(num_location[board][number])] == 5
			   ) {
				finished_boards[board] = true;
				n_boards_left -= 1;
			}
			if (n_boards_left == 0) {
				last_board = board;
				last_number = number;
				goto game_over;
			}
		}

//		std::cerr << "\n";
	}

game_over:
	std::cerr << "Board " << last_board << " won last"  << "\n";
	std::cerr << last_number;
	return std::make_tuple(last_board, last_number);
}

int get_winning_board_value(
		std::vector<int> numbers,
		std::map<int, std::map<int, std::map<int, int>>> board_contents,
		std::tuple<int, int> win) {
	std::vector<std::tuple<int, int>> full_locations;

	std::vector<bool> num_in_winning_board(100, false);
	int value = 0;
	for (int row = 0; row < 5; ++row) {
		for (int col = 0; col < 5; ++col) {
			num_in_winning_board[board_contents[std::get<0>(win)][row][col]] = true;
			value += board_contents[std::get<0>(win)][row][col];
		}
	}
//	std::cerr << "Sum: " << value << "\n";

	for (auto & number : numbers) {
		if (num_in_winning_board[number]) {
			value -= number;
		}
		if (number == std::get<1>(win)) {
			break;
		}
	}
	std::cerr << "Lille sum: " << value << "\n";

	return value * std::get<1>(win);
}

int part1(
		std::vector<int> numbers,
		std::map<int, std::map<int, std::map<int, int>>> board_contents,
		std::map<int, std::vector<int>> num_to_board,
		std::map<int, std::map<int, std::tuple<int, int>>> num_location,
		int n_boards
	) {
	return get_winning_board_value(
			numbers,
			board_contents,
			get_winning_board(
				numbers,
				num_to_board,
				num_location,
				n_boards
			)
	);
}

int part2(
		std::vector<int> numbers,
		std::map<int, std::map<int, std::map<int, int>>> board_contents,
		std::map<int, std::vector<int>> num_to_board,
		std::map<int, std::map<int, std::tuple<int, int>>> num_location,
		int n_boards
	) {
	return get_winning_board_value(
			numbers,
			board_contents,
			get_last_board(
				numbers,
				num_to_board,
				num_location,
				n_boards
			)
	);
}

int main() {
//	int n_numbers = 27;
	int n_numbers = 100;
	std::vector<int> numbers(n_numbers, 0);
	for (int i = 0; i<n_numbers; ++i) {
		std::cin >> numbers[i];
	}
	
	int i;
	int input;
	// num_to_board tells us which boards contain num
	// num_location[i_board] takes a number and returns
	// a tuple (row, col) of its location
	// board_contents[board][row][col] is the value at that
	// point
	std::map<int, std::vector<int>> num_to_board;
	std::map<int, std::map<int, std::tuple<int, int>>> num_location;
	std::map<int, std::map<int, std::map<int, int>>> board_contents;
	while (std::cin >> input) {
//		std::cerr << "Læg " << input << " i board " << i/25 << ", placering (" << ((i%25)/5) << ", " << i%5 << ")\n";
		// n_board = i/25
		// n_row = (i%25)/5
		// n_col = i%5
		num_to_board[input].push_back(i/25);
		num_location[i/25][input] = std::make_tuple((i%25)/5, i%5);
		board_contents[i/25][(i%25)/5][i%5] = input;
		++i;
	}
	std::cout << "Winning value: " << part1(
			numbers,
			board_contents,
			num_to_board,
			num_location,
			i/25
	) << "\n";
	std::cout << "Last value: " << part2(
			numbers,
			board_contents,
			num_to_board,
			num_location,
			i/25
	) << "\n";


	return 0;
}

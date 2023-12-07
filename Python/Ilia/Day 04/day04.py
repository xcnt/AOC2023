import re
import timeit

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def main():
    file_name = "Day 04\day04-prd.txt"
    file_data = parse_file(file_name)

    res_part_one = 0
    res_part_two = 0

    cards_pile = {}

    for line_number, line in enumerate(file_data, start=1):
        cards_pile[line_number] = cards_pile.get(line_number, 1)
        card_part_one = line.split('|')[0].split(':')[1]
        card_part_two = line.split('|')[1]

        elf_numbers = re.findall(r'\d+',card_part_one)
        win_numbers = re.findall(r'\d+',card_part_two)

        win_match = set(elf_numbers).intersection(win_numbers)
        winners_count = len(win_match)

        if winners_count > 0:
            res_part_one += 1 << (winners_count - 1)

        current_line_value = cards_pile[line_number]
        for i in range(line_number + 1, line_number + winners_count + 1):
            cards_pile[i] = cards_pile.get(i, 1) + current_line_value

    res_part_two = sum(cards_pile.values())

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

#Part One: 20855
#Part Two: 5489600
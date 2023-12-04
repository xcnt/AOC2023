import re

def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data

def solve_the_puzzle(s, part):
    calibration_dict = {
    "1":    "1",
    "2":    "2",
    "3":    "3",
    "4":    "4",
    "5":    "5",
    "6":    "6",
    "7":    "7",
    "8":    "8",
    "9":    "9"
}

    calibration_dictA = {
    "one":  "1",
    "two":  "2",
    "three":"3",
    "four": "4",
    "five": "5",
    "six":  "6",
    "seven":"7",
    "eight":"8",
    "nine": "9"
}
    # as we extend the rules on the part two, we need to update the initial dictionary
    if part == "two":
        calibration_dict.update(calibration_dictA)
    
    best_first_word = ""
    best_last_word = ""
    best_first_position = s.__len__()
    best_last_position = 0

    # walking through the dictionary and storing positions of all entries in *matches*
    for word in calibration_dict:
        matches = [match.start() for match in re.finditer(word, s)]
        if matches.__len__() == 0:
            continue
        
        # as it is should be the most left digit, we need ot find the minimal position
        if matches[0] <= best_first_position:
            # values in *matches* are sorted, so the smallest one is in [0]
            best_first_position = matches[0]
            best_first_word = word
 
        if matches[matches.__len__()-1] >= best_last_position:
            best_last_position = matches[matches.__len__()-1]
            best_last_word = word

    if best_first_word in calibration_dict and best_last_word in calibration_dict:
        return int(calibration_dict[best_first_word] + calibration_dict[best_last_word])
    else:
        return 0
  
def main():
    
    file_name = "Day 01\day01-prd.txt"
    file_data = parse_file(file_name)

    res_part_one = 0
    res_part_two = 0

    for line in file_data:
        res_part_one += solve_the_puzzle(line, part="one") #calibration_values
        res_part_two += solve_the_puzzle(line, part="two") #calibration_values

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    main()

#Part One: 56042
#Part Two: 55358
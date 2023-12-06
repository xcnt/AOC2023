# --- Day 3: Gear Ratios ---
import re

# the class may contain both - "part number" and "symbol"
class Schematic_obj:
    def __init__(self, value, line_num, start, end):
        self.value = value
        self.line_num = line_num
        self.start = start
        self.end = end

def parse_file(file_to_process):
    results_digt = []
    results_symb = []
    
    with open(file_to_process, 'r') as file:
        for line_number, line_content in enumerate(file, start=0):
            results_digt.extend(find_matches(line_content, r'\d+', line_number))
            results_symb.extend(find_matches(line_content, r'[^0-9.\n]', line_number))
    
    return results_digt, results_symb

def find_matches(line_content, pattern, line_number):
    matches = re.finditer(pattern, line_content)
    results = []
    
    for match in matches:
        start_position = match.start()
        end_position = match.end() - 1
        value = match.group()
        results.append(Schematic_obj(value, line_number, start_position, end_position))
    
    return results

def main():
    res_part_one = 0
    res_part_two = 0
    file_name = 'Day 03\day03-prd.txt'
    part_numbers,symbols = parse_file(file_name)

    for symbol in symbols:
        tmp = []
        for part in part_numbers:
            if abs(part.line_num - symbol.line_num) <= 1:
                if abs(symbol.start - part.start) <= 1 or abs(symbol.start - part.end) <= 1: 
                    res_part_one +=int(part.value)
                    if symbol.value == '*': # it is for Part two, looking for "gears"
                        tmp.append(int(part.value))
        if tmp.__len__() == 2:
            res_part_two += tmp[0] * tmp[1]      
  
    print('----------------------------')
    print('Part One:', res_part_one)
    print('Part Two:', res_part_two)

if __name__ == '__main__':
    main()

#Part One: 529618
#Part Two: 77509019
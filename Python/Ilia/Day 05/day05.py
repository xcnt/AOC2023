# --- Day 5: If You Give A Seed A Fertilizer ---
import timeit

class SeedMapping:
    def __init__(self, dst_range_start: int, src_range_start: int, range_len: int):
        self.dst_range_start = int(dst_range_start)
        self.src_range_start = int(src_range_start)
        self.range_len = int(range_len)

def get_intersection(obj_start, obj_range, map):
    start = max(obj_start, map.src_range_start)
    end = min(obj_start + obj_range, map.src_range_start + map.range_len)
    if start > end:
        return None
    else:
        return [start + (map.dst_range_start - map.src_range_start), end - start - 1]

def get_mapping_for_part_one(map,source):
    for X in map:
        if source >= X.src_range_start and source < X.src_range_start + X.range_len:
           return [X.dst_range_start + source - X.src_range_start]
   
    return [source]

def get_mapping_for_part_two(maps,source):
    new_mapping = []
    for map in maps:
        intersection = get_intersection(obj_start = source[0], obj_range = source[1], map = map) 
        if intersection is not None:
            new_mapping.append(intersection)

    if len(new_mapping) == 0:
        return [source]

    return new_mapping

def get_mapping(result, map_name, source, puzzle_part = 1):
    maps = []
    for S in source:
        if puzzle_part == 1:
            maps += get_mapping_for_part_one(result[map_name], source = S)

        if puzzle_part == 2:
            maps += get_mapping_for_part_two(result[map_name], source = S)

    return maps

def parse_file(file_to_process):
    file = open(file_to_process, mode='r')
    data: list[str] = file.read().split('\n')
    return data

def parse_data(file_data):
    seeds = []
    mapping_name = []
    maps = {}

    for line in file_data:
        if 'seeds:' in line:
            seeds = list(map(int, line.split(':')[1].split()))
        elif line.strip() == '':
            continue
        elif ':' in line:
            name, [] = line.split(':')
            maps[name] = set()
            mapping_name.append(name)
        else:
            src, dst, range = list(map(int, line.split()))
            maps[name].add(SeedMapping(src, dst, range))
            
    return seeds, maps, mapping_name

def main():
    file_name = 'Day 05\day05-prd.txt'
    file_data = parse_file(file_name)
    seeds, result, mapping_name = parse_data(file_data)

    tmp_res_one = seeds #seeds one by one
    tmp_res_two = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)] #seeds range
    for name in mapping_name:
        tmp_res_one = get_mapping(result, name, tmp_res_one, puzzle_part=1)
        tmp_res_two = get_mapping(result, name, tmp_res_two, puzzle_part=2)

    res_part_one = min(tmp_res_one)

    res_part_two = float('inf')
    for l_n in tmp_res_two:
        if l_n[0] < res_part_two:
            res_part_two = l_n[0]

    print('----------------------------')
    print('Part One:', res_part_one)
    print('Part Two:', res_part_two)

if __name__ == '__main__':
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print('Elapsed time:', end_time - start_time)

#Part One: 486613012
#Part Two: 56931769
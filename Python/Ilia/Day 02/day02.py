def parse_file(file_to_process):
    file = open(file_to_process, mode='r')
    data: list[str] = file.read().split('\n')
    return data

def parse_data(data):
    games = data.split(': ')[1].split('; ')

    result = []
    for game in games:
        d = {}
        for item in game.split(', '):
            count, color = item.split(' ')
            d[color] = int(count)
        result.append(d)

    return result

def is_game_possible(game):
    game_set =  {'red':  12, 'green':13, 'blue': 14}

    for attempt in game:
        if  ('red'   in attempt and attempt['red']   > game_set['red']  ) or \
            ('green' in attempt and attempt['green'] > game_set['green']) or \
            ('blue'  in attempt and attempt['blue']  > game_set['blue'] ):
            return False

    return True

def get_minimal_set_of_stone(game):
    b = max(g['blue']  for g in game if 'blue'  in g)
    r = max(g['red']   for g in game if 'red'   in g)
    g = max(g['green'] for g in game if 'green' in g)

    return b*r*g

def main():

    res_part_one = 0
    res_part_two = 0

    file_name = 'Day 02\day02-prd.txt'
    file_data = parse_file(file_name)
    game_counter = 1
    for line in file_data:
        game = parse_data(line)
        if is_game_possible(game):
            res_part_one+=game_counter
        
        res_part_two += get_minimal_set_of_stone(game)
        game_counter+=1

    print('----------------------------')
    print('Part One:', res_part_one)
    print('Part Two:', res_part_two)

if __name__ == '__main__':
    main()

#Part One: 2447
#Part Two: 56322
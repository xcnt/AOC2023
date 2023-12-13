import math
import timeit

def parse_file(file_to_process):
    with open(file_to_process, 'r') as f:
        time_list = f.readline().strip().split(':')[1].split()
        distance_list = f.readline().strip().split(':')[1].split()

    time_list = [int(time) for time in time_list]
    distance_list = [int(distance) for distance in distance_list]

    result = []
    for i in range(0, len(time_list)):
        result.append([time_list[i],distance_list[i]])

    return result

def find_the_edge(time, edge, dist, direction):
    while edge*(time - edge) >= dist:
        edge -= direction 

    while edge*(time - edge) <= dist:
        edge += direction 
    
    return edge

def solve_quadratic_polinom(a,b,c):
    D = b*b - 4 * a * c
    x1 = (-b + math.sqrt(D)) / 2*a
    x2 = (-b - math.sqrt(D)) / 2*a
    return min(x1, x2) , max(x1, x2)
  
#  math: solving quadratic polynomial a*x*x + b*x + c = 0
#  win_time * win_time + time * win_time - dist = 0
def get_winning_combination2(time, dist):
    edge_candidate = int(min(solve_quadratic_polinom(-1, time, -dist)))
    left_edge = find_the_edge(time, edge_candidate, dist, direction=1)
    right_edge = find_the_edge(time, time - left_edge, dist, direction=-1)
    res = abs(right_edge - left_edge + 1)

    return res

def main():
    file_name = "Day 06\day06-prd.txt"
    race_list = parse_file(file_name)

    res_part_one = 1
    for race in race_list:
        x = get_winning_combination2(time = race[0], dist = race[1])
        res_part_one *= x

    file_name = "Day 06\day06-prd2.txt"
    race_list = parse_file(file_name)

    res_part_two = 1
    for race in race_list:
        x = get_winning_combination2(time = race[0], dist = race[1])
        res_part_two *= x

    print("----------------------------")
    print("Part One:", res_part_one)
    print("Part Two:", res_part_two)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    print("Elapsed time:", end_time - start_time)

#Part One: 1312850
#Part Two: 36749103
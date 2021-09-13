from functools import reduce

# Take input data and return as 2D array of strings
def process_input(filename):
    # process input file
    data_array = []
    with open(filename) as f:
        for line in f:
            data_array.append(line.strip())
        return data_array

def get_tree_nums(grid, right, down):
    cols = len(grid[0])
    rows = len(grid)
    trees = 0
    current_coordinates = (right, down)
    while current_coordinates[1] < rows:
        # down is indexed first
        current_location = grid[current_coordinates[1]][current_coordinates[0]]
        #print('({current_coordinates[0]}, {current_coordinates[1]})  {current_location}'.format(current_coordinates=current_coordinates, current_location=current_location))
        if current_location == '#':
            trees += 1
        current_coordinates = ((current_coordinates[0] + right) % cols, current_coordinates[1] + down)
    return trees

def solve(data):
    # Part 1
    trees = get_tree_nums(data, 3, 1)
    print('Part 1 Num of Trees: ' + str(trees))

    # Part 2
    all_slopes = []
    all_slopes.append(get_tree_nums(data, 1, 1))
    all_slopes.append(get_tree_nums(data, 3, 1))
    all_slopes.append(get_tree_nums(data, 5, 1))
    all_slopes.append(get_tree_nums(data, 7, 1))
    all_slopes.append(get_tree_nums(data, 1, 2))

    print('Part 2 Product Slope Trees: ' + str(reduce(lambda x, y: x*y, all_slopes)))

def main(filename):
    solve(process_input(filename))

if __name__ == '__main__':
  main('example.txt')
  main('input.txt')